# bluroma-py
Attempt at making a Pleroma/Akkoma-like Bluesky client in Python. It's not gonna be good.

## To-do
A lot.

### Basic
List of things to implement before moving into a public beta
* Login
  * OAuth
  * Support for third-party PDSes (DONE)
  * Remember your session (mostly done)
* Client
  * Dashboard
  * Settings
  * All of the below
* Posts
  * Viewing posts
  * Making posts
  * Browsing replies
* Profiles
  * Seeing them
  * Interacting with them
* Interactions
  * Likes
  * Boosts
  * Blocks
  * Mutes
  * All of it
* Database
  * Initialization and migrations (done, migrations might need to be approved)
  * Store user sessions and data
* User settings
  * Basic Bluesky settings

### Future
Cool ideas that I feel would make up a "stable" release
* Interoperability / Federation (is this even possible with the atproto library?)
  * List links to ATproto tools
  * Show something for third-party AppViews
  * "Enhanced" Bridgy Fed posts (full post data is stored inside of the records, not used by Bluesky)
  * Account migrations
* Customization
  * Themes
  * Moderation
  * Opt-in post gating