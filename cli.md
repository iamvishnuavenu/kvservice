# Simple KV Service
Simple KV service written with Flask and Sqlite. Service can be accessed via HTTP and CLI Packaged in same repo.

Topic:  
[Index](readme.md) | [CLI](cli.md)| [Deployment](deployment.md)

---

## Local Usage:

1. Get a Key:
```
$ python kv.py get a
```
Output:

```
{
  "a": "b"
}
```

2. Get `ALL` Key:

```
$ python kv.py get
```
Output:

```
{
  "a": "b",
  "b": "2",
  "x": "some_data",
  "y": "other_data",
  "z": "another"
}
```

3. Watch the Changes:

```
$ python kv.py watch
```
Output:
```
{
  "a": "b",
  "b": "2",
  "x": "some_data",
  "y": "other_data",
  "z": "another"
}
```


## [WIP]: CLI Packaging
