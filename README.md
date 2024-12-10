# BQ PY App

A simple app that connects to GCP and calls the BigQuery API

## Auth commands

```
gcloud auth login
```

```
gcloud auth application-default login
```

## BigQuery commands

### CLI

```
bq load --source_format=NEWLINE_DELIMITED_JSON --autodetect=True PROJECT_ID:DATASET.TABLE_NAME FILE_NAME.json
```

```
bq load --source_format=NEWLINE_DELIMITED_JSON 'PROJECT_ID:DATASET.TABLE_NAME' --autodetect 'gs://BUCKET_NAME/FILE_NAME.json'
```

```
bq show  --format=prettyjson PROJECT_ID:DATASET.TABLE_NAME | jq -r '.schema.fields[] .name ' | sort
```

### Query

#### msg-with-reply-using-id

```
SELECT a.id,  a.body.content AS Question, b.body.content AS Replies
FROM `PROJECT_ID.DATASET.TABLE_NAME` a , unnest(a.replies) AS b
WHERE a.id = 1725460272017
ORDER BY a.id
```

#### msg-with-reply-merge

```
SELECT a.id, a.body.content AS Question, ARRAY_AGG(b.body.content IGNORE NULLS) AS Reply
FROM `PROJECT_ID.DATASET.TABLE_NAME` a, a.replies AS b
WHERE a.id = 1725460272017
GROUP BY a.id, a.body.content
ORDER BY a.id
```

```
create table PROJECT_ID.DATASET.TABLE_NAME as select * from PROJECT_ID.DATASET.TABLE_NAME where 1 = 2;
```

## JQ commands

```
cat FILE_NAME.json | head -n 1 | jq 'keys'
```

```
cat FILE_NAME.json | head -n 1 | jq '.id'
```

```
cat INPUT_FILE_NAME.json | jq -c '.[] | .' > OUTPUT_FILE_NAME.json
```

```
jq -c 'walk(if type == "object" and has("@odata.type") then del(."@odata.type") else . end)' input.json > output.json
```

## CLI commands

### Disk Usage Human Readable Summary:

```
du -hs FILE_NAME.json
```

### Word Count of Lines:

```
wc -l FILE_NAME.json
```

## Architecture Diagram
![arch_diagram](https://github.com/user-attachments/assets/4094919e-9e0f-40d8-a0fc-8c60c6038f1f)
