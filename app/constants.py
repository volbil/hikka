# Email types
EMAIL_ACTIVATION = "activation"
EMAIL_PASSWORD_RESET = "password_reset"

# CDN endpoing
CDN_ENDPOINT = "https://cdn.hikka.io"

# Sort options
SORT_DESC = "desc"
SORT_ASC = "asc"

# Watch list statuses
WATCH_PLANNED = "planned"
WATCH_WATCHING = "watching"
WATCH_COMPLETED = "completed"
WATCH_ON_HOLD = "on_hold"
WATCH_DROPPED = "dropped"

WATCH = [
    WATCH_PLANNED,
    WATCH_WATCHING,
    WATCH_COMPLETED,
    WATCH_ON_HOLD,
    WATCH_DROPPED,
]

# Watch list orders
WATCH_ORDER_MEDIA_TYPE = "media_type"
WATCH_ORDER_EPISODES = "episodes"
WATCH_ORDER_SCORE = "score"

# Seasons
SEASON_WINTER = "winter"
SEASON_SPRING = "spring"
SEASON_SUMMER = "summer"
SEASON_FALL = "fall"

RELEASE_STATUS_DISCONTINUED = "discontinued"
RELEASE_STATUS_ANNOUNCED = "announced"
RELEASE_STATUS_FINISHED = "finished"
RELEASE_STATUS_ONGOING = "ongoing"
RELEASE_STATUS_PAUSED = "paused"

MEDIA_TYPE_SPECIAL = "special"
MEDIA_TYPE_MOVIE = "movie"
MEDIA_TYPE_MUSIC = "music"
MEDIA_TYPE_OVA = "ova"
MEDIA_TYPE_ONA = "ona"
MEDIA_TYPE_TV = "tv"

AGE_RATING_R_PLUS = "r_plus"
AGE_RATING_PG_13 = "pg_13"
AGE_RATING_PG = "pg"
AGE_RATING_RX = "rx"
AGE_RATING_G = "g"
AGE_RATING_R = "r"

VIDEO_PROMO = "video_promo"
VIDEO_MUSIC = "video_music"

OST_OPENING = "opening"
OST_ENDING = "ending"

SOURCE_DIGITAL_MANGA = "digital_manga"
SOURCE_PICTURE_BOOK = "picture_book"
SOURCE_VISUAL_NOVEL = "visual_novel"
SOURCE_4_KOMA_MANGA = "4_koma_manga"
SOURCE_LIGHT_NOVEL = "light_novel"
SOURCE_CARD_GAME = "card_game"
SOURCE_WEB_MANGA = "web_manga"
SOURCE_ORIGINAL = "original"
SOURCE_MANGA = "manga"
SOURCE_MUSIC = "music"
SOURCE_NOVEL = "novel"
SOURCE_OTHER = "other"
SOURCE_RADIO = "radio"
SOURCE_GAME = "game"
SOURCE_BOOK = "book"

EXTERNAL_GENERAL = "general"
EXTERNAL_WATCH = "watch"

SEARCH_RESULT_SIZE = 15

# Meilisearch index names
SEARCH_INDEX_CHARACTERS = "content_characters"
SEARCH_INDEX_COMPANIES = "content_companies"
SEARCH_INDEX_PEOPLE = "content_people"  # Note: rename it to person (?)
SEARCH_INDEX_ANIME = "content_anime"

COMPANY_ANIME_PRODUCER = "producer"
COMPANY_ANIME_STUDIO = "studio"

EDIT_PENDING = "pending"
EDIT_ACCEPTED = "accepted"
EDIT_DENIED = "denied"
EDIT_CLOSED = "closed"

CONTENT_ANIME = "anime"
CONTENT_MANGA = "manga"
CONTENT_CHARACTER = "character"
CONTENT_COMPANY = "company"
CONTENT_EPISODE = "episode"
CONTENT_GENRE = "genre"
CONTENT_PERSON = "person"
CONTENT_STAFF = "staff"
CONTENT_SYSTEM_EDIT = "edit"
CONTENT_COLLECTION = "collection"
CONTENT_COMMENT = "comment"

# Roles
# ToDo: move to separate file (?)
ROLE_USER = "user"
ROLE_MODERATOR = "moderator"
ROLE_ADMIN = "admin"
ROLE_BANNED = "banned"
ROLE_NOT_ACTIVATED = "not_activated"

# Permissions
PERMISSION_EDIT_CREATE = "edit:create"
PERMISSION_EDIT_ACCEPT = "edit:accept"
PERMISSION_EDIT_REJECT = "edit:reject"
PERMISSION_EDIT_UPDATE = "edit:update"
PERMISSION_EDIT_UPDATE_MODERATOR = "edit:update_moderator"
PERMISSION_EDIT_CLOSE = "edit:close"
PERMISSION_EDIT_AUTO = "edit:auto"
PERMISSION_UPLOAD_AVATAR = "upload:avatar"
PERMISSION_UPLOAD_COVER = "upload:cover"
PERMISSION_COMMENT_WRITE = "comment:write"
PERMISSION_COMMENT_EDIT = "comment:edit"
PERMISSION_COMMENT_HIDE = "comment:hide"
PERMISSION_COMMENT_HIDE_ADMIN = "comment:hide_admin"
PERMISSION_COLLECTION_CREATE = "collection:create"
PERMISSION_COLLECTION_UPDATE = "collection:update"
PERMISSION_COLLECTION_DELETE = "collection:delete"
PERMISSION_COLLECTION_UPDATE_MODERATOR = "collection:update_moderator"
PERMISSION_COLLECTION_DELETE_MODERATOR = "collection:delete_moderator"
PERMISSION_VOTE_SET = "vote:set"

# Role permissions
ROLES = {
    ROLE_USER: [
        PERMISSION_EDIT_CREATE,
        PERMISSION_EDIT_UPDATE,
        PERMISSION_EDIT_CLOSE,
        PERMISSION_UPLOAD_AVATAR,
        PERMISSION_UPLOAD_COVER,
        PERMISSION_COMMENT_WRITE,
        PERMISSION_COMMENT_EDIT,
        PERMISSION_COMMENT_HIDE,
        PERMISSION_VOTE_SET,
        PERMISSION_COLLECTION_CREATE,
        PERMISSION_COLLECTION_UPDATE,
        PERMISSION_COLLECTION_DELETE,
    ],
    ROLE_MODERATOR: [
        PERMISSION_EDIT_CREATE,
        PERMISSION_EDIT_ACCEPT,
        PERMISSION_EDIT_REJECT,
        PERMISSION_EDIT_UPDATE,
        PERMISSION_EDIT_CLOSE,
        PERMISSION_EDIT_AUTO,
        PERMISSION_EDIT_UPDATE_MODERATOR,
        PERMISSION_UPLOAD_AVATAR,
        PERMISSION_UPLOAD_COVER,
        PERMISSION_COMMENT_WRITE,
        PERMISSION_COMMENT_EDIT,
        PERMISSION_COMMENT_HIDE,
        PERMISSION_COMMENT_HIDE_ADMIN,
        PERMISSION_VOTE_SET,
        PERMISSION_COLLECTION_CREATE,
        PERMISSION_COLLECTION_UPDATE,
        PERMISSION_COLLECTION_DELETE,
        PERMISSION_COLLECTION_UPDATE_MODERATOR,
        PERMISSION_COLLECTION_DELETE_MODERATOR,
    ],
    ROLE_ADMIN: [
        PERMISSION_EDIT_CREATE,
        PERMISSION_EDIT_ACCEPT,
        PERMISSION_EDIT_REJECT,
        PERMISSION_EDIT_UPDATE,
        PERMISSION_EDIT_CLOSE,
        PERMISSION_EDIT_AUTO,
        PERMISSION_EDIT_UPDATE_MODERATOR,
        PERMISSION_UPLOAD_AVATAR,
        PERMISSION_UPLOAD_COVER,
        PERMISSION_COMMENT_WRITE,
        PERMISSION_COMMENT_EDIT,
        PERMISSION_COMMENT_HIDE,
        PERMISSION_COMMENT_HIDE_ADMIN,
        PERMISSION_VOTE_SET,
        PERMISSION_COLLECTION_CREATE,
        PERMISSION_COLLECTION_UPDATE,
        PERMISSION_COLLECTION_DELETE,
        PERMISSION_COLLECTION_UPDATE_MODERATOR,
        PERMISSION_COLLECTION_DELETE_MODERATOR,
    ],
    ROLE_NOT_ACTIVATED: [
        PERMISSION_UPLOAD_AVATAR,
        PERMISSION_UPLOAD_COVER,
    ],
    ROLE_BANNED: [],
}

# Upload types
UPLOAD_AVATAR = "avatar"
UPLOAD_COVER = "cover"

# Todo types
TODO_ANIME_SYNOPSIS_UA = "synopsis_ua"
TODO_ANIME_TITLE_UA = "title_ua"

# Log types
LOG_FAVOURITE_ANIME = "favourite_anime_add"
LOG_FAVOURITE_ANIME_REMOVE = "favourite_anime_remove"
LOG_FAVOURITE = "favourite_add"
LOG_FAVOURITE_REMOVE = "favourite_remove"
LOG_COMMENT_WRITE = "comment_write"
LOG_COMMENT_EDIT = "comment_edit"
LOG_COMMENT_HIDE = "comment_hide"
LOG_COMMENT_VOTE = "comment_vote"
LOG_FOLLOW = "follow"
LOG_UNFOLLOW = "unfollow"
LOG_UPLOAD = "upload"
LOG_SIGNUP = "signup"
LOG_LOGIN = "login"
LOG_LOGIN_OAUTH = "login_oauth"
LOG_ACTIVATION = "activation"
LOG_ACTIVATION_RESEND = "activation_resend"
LOG_PASSWORD_RESET = "password_reset"
LOG_PASSWORD_RESET_CONFIRM = "password_reset_confirm"
LOG_EDIT_CREATE = "edit_create"
LOG_EDIT_UPDATE = "edit_update"
LOG_EDIT_CLOSE = "edit_close"
LOG_EDIT_ACCEPT = "edit_accept"
LOG_EDIT_ACCEPT_AUTO = "edit_accept_auto"
LOG_EDIT_DENY = "edit_deny"
LOG_WATCH_CREATE = "watch_create"
LOG_WATCH_UPDATE = "watch_update"
LOG_WATCH_DELETE = "watch_delete"
LOG_SETTINGS_DESCRIPTION = "settings_description"
LOG_SETTINGS_USERNAME = "settings_username"
LOG_SETTINGS_EMAIL = "settings_email"
LOG_SETTINGS_PASSWORD = "settings_password"
LOG_SETTINGS_IMPORT = "settings_import"
LOG_COLLECTION_CREATE = "collection_create"
LOG_COLLECTION_UPDATE = "collection_update"
LOG_COLLECTION_DELETE = "collection_delete"
LOG_VOTE_SET = "vote_set"

# History types
HISTORY_WATCH = "watch"
HISTORY_WATCH_DELETE = "watch_delete"
HISTORY_FAVOURITE_ANIME = "favourite_anime_add"
HISTORY_FAVOURITE_ANIME_REMOVE = "favourite_anime_remove"
HISTORY_WATCH_IMPORT = "watch_import"

# Notification types
NOTIFICATION_COMMENT_REPLY = "comment_reply"
NOTIFICATION_COMMENT_VOTE = "comment_vote"
NOTIFICATION_COMMENT_TAG = "comment_tag"
NOTIFICATION_COLLECTION_COMMENT = "collection_comment"
NOTIFICATION_EDIT_COMMENT = "edit_comment"
NOTIFICATION_EDIT_ACCEPTED = "edit_accepted"
NOTIFICATION_EDIT_DENIED = "edit_denied"
NOTIFICATION_EDIT_UPDATED = "edit_updated"
NOTIFICATION_HIKKA_UPDATE = "hikka_update"

# Activity intervals
INTERVAL_DAY = "day"

# Collections
COLLECTION_PUBLIC = "public"
COLLECTION_UNLISTED = "unlisted"
COLLECTION_PRIVATE = "private"
