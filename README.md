# ms-teams-actions

Github Actions for sending a message to Microsoft Teams channel, built with Python3 and [pymsteams](https://github.com/rveachkc/pymsteams)

## Inputs

- `webhook_uri` (**Required**): Incoming webhook URI to Teams
- `title` (Optional): Title of the message
- `color` (Optional): Theme color of the message in hex form
- `summary` (Optional): Message summary
- `text` (Optional): Text of the message
- `link_buttons` (Optional): JSON double-deep array, where inner array consists of 'button text' and 'button url'. If actions exist, it goes to the end.
- `theme_color` (Optional): Message theme color
- `sections` (Optional): JSON array of card section objects
- `actions` (Optional): JSON array of potential action objects

## Example Usage

```yaml
steps:
  name: Send a message to Microsoft Teams
  uses: sjquant/ms-teams-actions@main
  with:
    webhook_uri: ${{ secrets.WEBHOOK_URI }}
    title: <Message Title>
    summary: <Message Summary>
    text: <Message Text>
    color: <Message Theme Color>
    sections: '[{ "activityTitle": "hello world" }, { ... }]'
    actions: '[{ "@type": "OpenUri", "name": "lorem ipsum", "targets": [{ "os": "default", "uri": "https://localhost" }] }, { ... }]'
    link_buttons: '[["Open Github", "https://github.com"], ["Open Facebook", "https://facebook.com"]]'
```

> For more details about how to build connector card, see this reference : [https://docs.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/cards/cards-reference#office-365-connector-card](https://docs.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/cards/cards-reference#office-365-connector-card)

## License

[MIT](./LICENSE)
