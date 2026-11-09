Update the Schema
cd sql/schema
goose postgres "postgres://postgres@localhost:5432/chirpy?sslmode=disable" up

sqlc generate
