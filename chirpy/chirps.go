package main

import (
	"encoding/json"
	"net/http"
	"strings"
	"unicode"
	"unicode/utf8"
)

type validateChirpRequest struct {
	Body string `json:"body"`
}

func handlerValidateChirp(w http.ResponseWriter, r *http.Request) {
	request := validateChirpRequest{}
	if err := json.NewDecoder(r.Body).Decode(&request); err != nil {
		respondWithError(w, http.StatusBadRequest, "Something went wrong")
		return
	}

	if utf8.RuneCountInString(request.Body) > 140 {
		respondWithError(w, http.StatusBadRequest, "Chirp is too long")
		return
	}

	respondWithJSON(w, http.StatusOK, map[string]string{"cleaned_body": cleanChirp(request.Body)})
}

func cleanChirp(body string) string {
	var cleaned strings.Builder
	for index := 0; index < len(body); {
		runeValue, size := utf8.DecodeRuneInString(body[index:])
		if unicode.IsSpace(runeValue) {
			cleaned.WriteString(body[index : index+size])
			index += size
			continue
		}

		start := index
		for index < len(body) {
			runeValue, runeSize := utf8.DecodeRuneInString(body[index:])
			if unicode.IsSpace(runeValue) {
				break
			}
			index += runeSize
		}

		word := body[start:index]
		if strings.EqualFold(word, "kerfuffle") || strings.EqualFold(word, "sharbert") || strings.EqualFold(word, "fornax") {
			cleaned.WriteString("****")
		} else {
			cleaned.WriteString(word)
		}
	}

	return cleaned.String()
}

func respondWithError(w http.ResponseWriter, code int, msg string) {
	respondWithJSON(w, code, map[string]string{"error": msg})
}

func respondWithJSON(w http.ResponseWriter, code int, payload interface{}) {
	data, err := json.Marshal(payload)
	if err != nil {
		http.Error(w, "Internal Server Error", http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(code)
	w.Write(data)
}
