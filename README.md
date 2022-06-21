# confitec_teste Flask Application

Awesome confitec_teste created by filipelira1

## Installation

From source:

```bash
git clone https://github.com/filipelira1/confitec-teste confitec_teste
cd confitec_teste
make install
```

From pypi:

```bash
pip install confitec_teste
```

## Config Project

Copy the file named `sample.env` to `.env` and fill env variables

```bash
$ cp .sample.env .env
```

## Executing

This application has a CLI interface that extends the Flask CLI.

Just run:

```bash
$ confitec_teste
```

or

```bash
$ python -m confitec_teste
```

To see the help message and usage instructions.

Go to:

  - user: admin, senha: 1234
- API GET:
  - http://localhost:5000/api/v1/Roberto Carlos/top-10-songs
  - http://localhost:5000/api/v1/Maroon 5/top-10-songs/
  - http://localhost:5000/api/v1/Justin Timberlake/top-10-songs
  - http://localhost:5000/api/v1/Shakira/top-10-songs


> **Note**: You can also use `flask run` to run the application.

## Roadmap

- [x] - Search Top 10 Musics by artist
- [] - Save transaction in DyanmoDB
- [] - Save cache in Redis
- [] - Write tests
