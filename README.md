# BreakingBad API *in GraphQL*
**Preface** | This repo has only purpose to make experiments with GraphQL by [Strawberry](https://github.com/strawberry-graphql/strawberry).
Dataset is retrieved from [BreakingBad Api](https://github.com/timbiles/Breaking-Bad--API).

### Install dependencies
    poetry install

### Start the server
```sh
cd breakingbad/
poetry run strawberry server breakingbad
```

### Play with payloads!
#### Basic query
Retrieve all characters
```js
{
  characters {
    items {
      name
      nickname
      occupation
    }
  }
}
```
All episodes with extra information on characters
```js
{
  episodes {
    items {
      title
      season
      series
      characters {
        name
        nickname
      }
    }
  }
}
```
#### Filtering [wip]
```js
{
  deaths(responsible:{nickname: "Heisenberg"}) {
    items{
      death
      cause
    }
  }
}
```

#### Pagination
**Preface** | Pagination technique used is "**Cursor Pagination**" to obtain more performance and readability than Connection type skipping edge nodes


- `after` indicates the offset of query. [ `after` must be >= 0 ]
- `first` indicate the number of results after `after` element do you want [ `after` must be set if you use `first` ]
```js
{
  deaths(after:2,first:4) {
    next
    items{
      deathId
      cause
      death
      lastWords
      responsible
    }
  }
}
```
 