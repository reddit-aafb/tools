import sgqlc.types
import sgqlc.types.datetime
import sgqlc.types.relay


aaf_schema = sgqlc.types.Schema()


# Unexport Node/PageInfo, let schema re-declare them
aaf_schema -= sgqlc.types.relay.Node
aaf_schema -= sgqlc.types.relay.PageInfo



########################################################################
# Scalars and Enumerations
########################################################################
Boolean = sgqlc.types.Boolean

class CoachPosition(sgqlc.types.Enum):
    __schema__ = aaf_schema
    __choices__ = ('HEAD_COACH', 'OFFENSIVE_COORDINATOR', 'DEFENSIVE_COORDINATOR', 'SPECIAL_TEAMS_COACH')


class CoinTossChoiceOption(sgqlc.types.Enum):
    __schema__ = aaf_schema
    __choices__ = ('RECEIVE', 'KICK', 'DEFER')


class Color(sgqlc.types.Scalar):
    __schema__ = aaf_schema


Date = sgqlc.types.datetime.Date

DateTime = sgqlc.types.datetime.DateTime

Float = sgqlc.types.Float

class GamePhase(sgqlc.types.Enum):
    __schema__ = aaf_schema
    __choices__ = ('PLAYING', 'HALFTIME', 'SUSPENDED', 'COMPLETE', 'PREGAME')


ID = sgqlc.types.ID

Int = sgqlc.types.Int

class LongInt(sgqlc.types.Scalar):
    __schema__ = aaf_schema


class OfficialPosition(sgqlc.types.Enum):
    __schema__ = aaf_schema
    __choices__ = ('REPLAY_OFFICIAL', 'SUPERVISOR', 'CENTER_JUDGE', 'GAME_CLOCK_OPERATOR', 'REFEREE', 'DOWN_JUDGE', 'BACK_JUDGE', 'UMPIRE', 'SIDE_JUDGE', 'PLAY_CLOCK_OPERATOR', 'VIDEO_EVALUATOR', 'LINE_JUDGE', 'FIELD_JUDGE', 'REPLAY_COMMUNICATOR', 'COACH_TO_PLAYER_CUTOFF_OFFICIAL', 'TECHNICIAN')


class Platoon(sgqlc.types.Enum):
    __schema__ = aaf_schema
    __choices__ = ('OFFENSE', 'DEFENSE', 'SPECIAL_TEAMS')


class PlayStatSubtype(sgqlc.types.Enum):
    __schema__ = aaf_schema
    __choices__ = ('MISCELLANEOUS', 'REGULAR', 'SPECIAL_TEAMS')


class PlayStatType(sgqlc.types.Enum):
    __schema__ = aaf_schema
    __choices__ = ('INTERCEPTION_RETURN_YARDS_WITHOUT_INTERCEPTION', 'TACKLE', 'PASS_INTERCEPTED', 'PUNTING_YARDS_WITH_TOUCHBACK', 'FOURTH_DOWN_UNCONVERTED', 'PASSING_YARDS_FOR_TOUCHDOWN_WITHOUT_PASS', 'FUMBLE', 'PENALTY_YARDS', 'FIELD_GOAL_BLOCKED', 'THIRD_DOWN_CONVERTED', 'TACKLE_FOR_LOSS', 'RECEIVING_YARDS', 'FIRST_DOWN_BY_PASSING', 'SACK_YARDS_OFFENSE', 'PUNT_RETURN_YARDS_FOR_TOUCHDOWN_WITHOUT_RETURN', 'PUNTING_YARDS', 'QUARTERBACK_HIT', 'PUNT_BLOCKED', 'PUNTING_YARDS_INTO_END_ZONE_WITHOUT_TOUCHBACK', 'RECEIVING_YARDS_WITHOUT_RECEPTION', 'TACKLE_ASSIST', 'AIR_YARDS_INCOMPLETE', 'TWO_POINT_PASS_RECEPTION_GOOD', 'OWN_FUMBLE_RECOVERY_YARDS_FOR_TOUCHDOWN_WITHOUT_RECOVERY', 'PASS_TARGET', 'SAFETY', 'THIRD_DOWN_UNCONVERTED', 'OWN_FUMBLE_RECOVERY_YARDS_WITHOUT_RECOVERY', 'OPPOSING_FIELD_GOAL_BLOCKED', 'ASSISTED_TACKLE', 'TWO_POINT_RUSH_GOOD', 'SACK_YARDS_DEFENSE', 'OPPONENT_FUMBLE_FORCED', 'RUSHING_YARDS_FOR_TOUCHDOWN_WITHOUT_RUSH', 'RECEIVING_YARDS_FOR_TOUCHDOWN', 'PUNT_INSIDE_20', 'OPPONENT_FUMBLE_RECOVERY_YARDS_FOR_TOUCHDOWN_WITHOUT_RECOVERY', 'PUNT_RETURN_YARDS_WITHOUT_RETURN', 'MISCELLANEOUS_YARDS_FOR_TOUCHDOWN', 'OWN_FUMBLE_RECOVERY_YARDS_FOR_TOUCHDOWN', 'MISCELLANEOUS_YARDS', 'INTERCEPTION_RETURN_YARDS_FOR_TOUCHDOWN_WITHOUT_INTERCEPTION', 'FIELD_GOAL_YARDS', 'PUNT_RETURN_YARDS', 'INTERCEPTION_RETURN_YARDS', 'AIR_YARDS_COMPLETE', 'FUMBLE_FORCED', 'OPPONENT_FUMBLE_RECOVERY_YARDS_FOR_TOUCHDOWN', 'RUSHING_YARDS', 'OWN_FUMBLE_RECOVERY_YARDS', 'RUSHING_YARDS_WITHOUT_RUSH', 'TWO_POINT_PASS_GOOD', 'OPPONENT_FUMBLE_RECOVERY_YARDS_WITHOUT_RECOVERY', 'PASSING_YARDS', 'FIRST_DOWN_BY_PENALTY', 'RECEIVING_YARDS_FOR_TOUCHDOWN_WITHOUT_RECEPTION', 'OPPONENT_FUMBLE_RECOVERY_YARDS', 'PASSING_YARDS_WITHOUT_PASS', 'PASSING_YARDS_FOR_TOUCHDOWN', 'PUNT_RETURN_YARDS_FOR_TOUCHDOWN', 'HALF_SACK_YARDS_DEFENSE', 'FOURTH_DOWN_CONVERTED', 'INTERCEPTION_RETURN_YARDS_FOR_TOUCHDOWN', 'FIELD_GOAL_MISSED_YARDS', 'PASS_INCOMPLETE', 'PASS_DEFENSE', 'FIRST_DOWN_BY_RUSHING', 'YARDS_AFTER_CATCH', 'RUSHING_YARDS_FOR_TOUCHDOWN')


class PlayType(sgqlc.types.Enum):
    __schema__ = aaf_schema
    __choices__ = ('KICKOFF', 'PENALTY', 'PUNT', 'RUSH', 'PASS', 'FIELD_GOAL')


class PlayerPosition(sgqlc.types.Enum):
    __schema__ = aaf_schema
    __choices__ = ('WIDE_RECEIVER', 'RUNNING_BACK', 'PUNTER', 'OFFENSIVE_TACKLE', 'DEFENSIVE_LINEMAN', 'HALFBACK', 'NOSE_TACKLE', 'HOLDER', 'STRONG_SAFETY', 'DEFENSIVE_END', 'FULLBACK', 'OFFENSIVE_LINEMAN', 'OFFENSIVE_GUARD', 'PUNT_RETURNER', 'MIDDLE_LINEBACKER', 'LINEBACKER', 'KICKER', 'TIGHT_END', 'CENTER', 'LONG_SNAPPER', 'DEFENSIVE_BACK', 'OUTSIDE_LINEBACKER', 'CORNERBACK', 'QUARTERBACK', 'DEFENSIVE_TACKLE', 'SAFETY', 'FREE_SAFETY')


class PlayerRosterStatus(sgqlc.types.Enum):
    __schema__ = aaf_schema
    __choices__ = ('WAIVER_REQUEST', 'RESERVE_TENDERED', 'RESERVE_PHYSICALLY_UNABLE_TO_PLAY', 'RESERVE_NONFOOTBALL_INJURY', 'RESERVE_MILITARY', 'RIGHTS_LIST', 'RESERVE_RETIRED', 'RESERVE_INJURED', 'ACTIVE_LIST', 'OTHER', 'RESERVE_NONFOOTBALL_ILLNESS', 'FREE_AGENT_ALLOCATED', 'TERMINATION_OF_RIGHTS', 'RESERVE_OTHER_LEAGUE', 'RESERVE_DID_NOT_REPORT', 'FREE_AGENT_UNALLOCATED', 'RESERVE_SUSPENDED')


class Possession(sgqlc.types.Enum):
    __schema__ = aaf_schema
    __choices__ = ('NONE', 'HOME_TEAM', 'AWAY_TEAM')


class PrincipalWind(sgqlc.types.Enum):
    __schema__ = aaf_schema
    __choices__ = ('SOUTH_EAST', 'NORTH_WEST', 'SOUTH_WEST', 'NORTH', 'SOUTH', 'EAST', 'WEST', 'NORTH_EAST')


class SeasonAggregatedTeamStatsAggregator(sgqlc.types.Enum):
    __schema__ = aaf_schema
    __choices__ = ('MIN', 'MAX', 'SUM')


String = sgqlc.types.String

class Subseason(sgqlc.types.Enum):
    __schema__ = aaf_schema
    __choices__ = ('PRE', 'REGULAR', 'POST')


class TeamBackgroundStyle(sgqlc.types.Enum):
    __schema__ = aaf_schema
    __choices__ = ('BANNER_DARK',)


class TeamLogoStyle(sgqlc.types.Enum):
    __schema__ = aaf_schema
    __choices__ = ('LIGHT_BACKGROUND', 'DARK_BACKGROUND')


class TeamWordmarkStyle(sgqlc.types.Enum):
    __schema__ = aaf_schema
    __choices__ = ('DARK_BACKGROUND', 'LIGHT_BACKGROUND')


class TimeoutType(sgqlc.types.Enum):
    __schema__ = aaf_schema
    __choices__ = ('OFFICIAL', 'TEAM')


class UserRole(sgqlc.types.Enum):
    __schema__ = aaf_schema
    __choices__ = ('AV_READER', 'NEWS_EDITOR', 'PERSONNEL_READER', 'PERSONNEL_WRITER', 'STADIUM', 'AV_SERVICE', 'ADMIN', 'AV_WRITER', 'TEAM_PERSONNEL_WRITER')


class UserTokenType(sgqlc.types.Enum):
    __schema__ = aaf_schema
    __choices__ = ('REGISTRATION', 'PASSWORD_RESET')


class YardLineTeam(sgqlc.types.Enum):
    __schema__ = aaf_schema
    __choices__ = ('AWAY_TEAM', 'NONE', 'HOME_TEAM')



########################################################################
# Input Objects
########################################################################
class AVProgramInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    game_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='gameId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    is_private = sgqlc.types.Field(Boolean, graphql_name='isPrivate')
    hls_event_master_playlist_url = sgqlc.types.Field(String, graphql_name='hlsEventMasterPlaylistURL')


class AVProgramPatchInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    is_private = sgqlc.types.Field(Boolean, graphql_name='isPrivate')
    name = sgqlc.types.Field(String, graphql_name='name')
    hls_event_master_playlist_url = sgqlc.types.Field(String, graphql_name='hlsEventMasterPlaylistURL')
    thumbnail_file_id = sgqlc.types.Field(ID, graphql_name='thumbnailFileId')


class AVStreamInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    bitrate = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='bitrate')
    codecs = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='codecs')
    game_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='gameId')
    program_id = sgqlc.types.Field(ID, graphql_name='programId')
    maximum_segment_duration_milliseconds = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='maximumSegmentDurationMilliseconds')
    video_height = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='videoHeight')
    video_width = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='videoWidth')
    is_live = sgqlc.types.Field(Boolean, graphql_name='isLive')


class AVStreamPatchInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    codecs = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='codecs')
    time_adjustment_milliseconds = sgqlc.types.Field(Int, graphql_name='timeAdjustmentMilliseconds')
    is_live = sgqlc.types.Field(Boolean, graphql_name='isLive')
    program_id = sgqlc.types.Field(ID, graphql_name='programId')


class AVStreamSegmentReplicaInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    duration_milliseconds = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='durationMilliseconds')
    discontinuity = sgqlc.types.Field(Boolean, graphql_name='discontinuity')
    time = sgqlc.types.Field(DateTime, graphql_name='time')
    stream_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='streamId')
    segment_number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='segmentNumber')


class AddressInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    line1 = sgqlc.types.Field(String, graphql_name='line1')
    line2 = sgqlc.types.Field(String, graphql_name='line2')
    locality = sgqlc.types.Field(String, graphql_name='locality')
    administrative_area = sgqlc.types.Field(String, graphql_name='administrativeArea')
    administrative_area_abbreviation = sgqlc.types.Field(String, graphql_name='administrativeAreaAbbreviation')
    postal_code = sgqlc.types.Field(String, graphql_name='postalCode')
    country_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='countryCode')


class AgentInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    phone_number = sgqlc.types.Field(String, graphql_name='phoneNumber')
    birth_date = sgqlc.types.Field(Date, graphql_name='birthDate')
    personnel_notes = sgqlc.types.Field(String, graphql_name='personnelNotes')
    height_millimeters = sgqlc.types.Field(Int, graphql_name='heightMillimeters')
    avatar_file_id = sgqlc.types.Field(ID, graphql_name='avatarFileId')
    phone_number_alternative = sgqlc.types.Field(String, graphql_name='phoneNumberAlternative')
    common_name = sgqlc.types.Field('PersonNameInput', graphql_name='commonName')
    weight_grams = sgqlc.types.Field(Int, graphql_name='weightGrams')
    legal_name = sgqlc.types.Field('PersonNameInput', graphql_name='legalName')
    email_address = sgqlc.types.Field(String, graphql_name='emailAddress')
    biography = sgqlc.types.Field(String, graphql_name='biography')
    email_address_alternative = sgqlc.types.Field(String, graphql_name='emailAddressAlternative')


class AgentPatchInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    avatar_file_id = sgqlc.types.Field(ID, graphql_name='avatarFileId')
    birth_date = sgqlc.types.Field(Date, graphql_name='birthDate')
    personnel_notes = sgqlc.types.Field(String, graphql_name='personnelNotes')
    height_millimeters = sgqlc.types.Field(Int, graphql_name='heightMillimeters')
    phone_number_alternative = sgqlc.types.Field(String, graphql_name='phoneNumberAlternative')
    biography = sgqlc.types.Field(String, graphql_name='biography')
    legal_name = sgqlc.types.Field('PersonNameInput', graphql_name='legalName')
    common_name = sgqlc.types.Field('PersonNameInput', graphql_name='commonName')
    email_address_alternative = sgqlc.types.Field(String, graphql_name='emailAddressAlternative')
    weight_grams = sgqlc.types.Field(Int, graphql_name='weightGrams')
    email_address = sgqlc.types.Field(String, graphql_name='emailAddress')
    phone_number = sgqlc.types.Field(String, graphql_name='phoneNumber')


class BallTelemetrySampleInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    ball_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='ballId')
    time = sgqlc.types.Field(DateTime, graphql_name='time')
    position_meters = sgqlc.types.Field('Point3DInput', graphql_name='positionMeters')
    orientation = sgqlc.types.Field('QuaternionInput', graphql_name='orientation')


class CoachInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    biography = sgqlc.types.Field(String, graphql_name='biography')
    birth_date = sgqlc.types.Field(Date, graphql_name='birthDate')
    team_id = sgqlc.types.Field(ID, graphql_name='teamId')
    common_name = sgqlc.types.Field('PersonNameInput', graphql_name='commonName')
    position = sgqlc.types.Field(CoachPosition, graphql_name='position')
    career_summary = sgqlc.types.Field(String, graphql_name='careerSummary')
    height_millimeters = sgqlc.types.Field(Int, graphql_name='heightMillimeters')
    personnel_notes = sgqlc.types.Field(String, graphql_name='personnelNotes')
    weight_grams = sgqlc.types.Field(Int, graphql_name='weightGrams')
    avatar_file_id = sgqlc.types.Field(ID, graphql_name='avatarFileId')
    title = sgqlc.types.Field(String, graphql_name='title')
    legal_name = sgqlc.types.Field('PersonNameInput', graphql_name='legalName')


class CoachPatchInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    birth_date = sgqlc.types.Field(Date, graphql_name='birthDate')
    weight_grams = sgqlc.types.Field(Int, graphql_name='weightGrams')
    avatar_file_id = sgqlc.types.Field(ID, graphql_name='avatarFileId')
    career_summary = sgqlc.types.Field(String, graphql_name='careerSummary')
    title = sgqlc.types.Field(String, graphql_name='title')
    legal_name = sgqlc.types.Field('PersonNameInput', graphql_name='legalName')
    height_millimeters = sgqlc.types.Field(Int, graphql_name='heightMillimeters')
    biography = sgqlc.types.Field(String, graphql_name='biography')
    personnel_notes = sgqlc.types.Field(String, graphql_name='personnelNotes')
    common_name = sgqlc.types.Field('PersonNameInput', graphql_name='commonName')
    team_id = sgqlc.types.Field(ID, graphql_name='teamId')
    position = sgqlc.types.Field(CoachPosition, graphql_name='position')


class CoinTossChoiceInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    direction = sgqlc.types.Field(PrincipalWind, graphql_name='direction')
    option = sgqlc.types.Field(sgqlc.types.non_null(CoinTossChoiceOption), graphql_name='option')


class CoinTossInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    winning_choice = sgqlc.types.Field(sgqlc.types.non_null(CoinTossChoiceInput), graphql_name='winningChoice')
    losing_choice = sgqlc.types.Field(sgqlc.types.non_null(CoinTossChoiceInput), graphql_name='losingChoice')
    winning_team_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='winningTeamId')
    before_quarter = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='beforeQuarter')


class DivisionInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    abbreviation = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='abbreviation')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class EventAvailabilityInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    short_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='shortName')
    url = sgqlc.types.Field(String, graphql_name='url')
    logo_file_id = sgqlc.types.Field(ID, graphql_name='logoFileId')


class GameBallInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    game_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='gameId')
    ball_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='ballId')


class GameClockInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    game_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='gameId')
    seconds = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='seconds')
    time = sgqlc.types.Field(DateTime, graphql_name='time')


class GameInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    telemetry_xdirection = sgqlc.types.Field(PrincipalWind, graphql_name='telemetryXDirection')
    time = sgqlc.types.Field(DateTime, graphql_name='time')
    time_to_be_determined = sgqlc.types.Field(Boolean, graphql_name='timeToBeDetermined')
    home_team_id = sgqlc.types.Field(ID, graphql_name='homeTeamId')
    away_team_id = sgqlc.types.Field(ID, graphql_name='awayTeamId')
    season_id = sgqlc.types.Field(ID, graphql_name='seasonId')
    ticketing_website_url = sgqlc.types.Field(String, graphql_name='ticketingWebsiteURL')
    stadium_id = sgqlc.types.Field(ID, graphql_name='stadiumId')


class GamePatchInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    away_team_id = sgqlc.types.Field(ID, graphql_name='awayTeamId')
    subseason = sgqlc.types.Field(Subseason, graphql_name='subseason')
    availability = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(EventAvailabilityInput)), graphql_name='availability')
    vod_start_time = sgqlc.types.Field(DateTime, graphql_name='vodStartTime')
    default_avprogram_id = sgqlc.types.Field(ID, graphql_name='defaultAVProgramId')
    time = sgqlc.types.Field(DateTime, graphql_name='time')
    ticketing_website_url = sgqlc.types.Field(String, graphql_name='ticketingWebsiteURL')
    duration_milliseconds = sgqlc.types.Field(Int, graphql_name='durationMilliseconds')
    stadium_id = sgqlc.types.Field(ID, graphql_name='stadiumId')
    telemetry_xdirection = sgqlc.types.Field(PrincipalWind, graphql_name='telemetryXDirection')
    hls_event_master_playlist_url = sgqlc.types.Field(String, graphql_name='hlsEventMasterPlaylistURL')
    home_team_id = sgqlc.types.Field(ID, graphql_name='homeTeamId')
    coin_tosses = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CoinTossInput)), graphql_name='coinTosses')
    time_to_be_determined = sgqlc.types.Field(Boolean, graphql_name='timeToBeDetermined')


class GamePlayClockInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    game_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='gameId')
    seconds = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='seconds')
    time = sgqlc.types.Field(DateTime, graphql_name='time')


class GamePlayerFormationDepthInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    team_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='teamId')
    depth = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='depth')
    formation = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='formation')
    platoon = sgqlc.types.Field(sgqlc.types.non_null(Platoon), graphql_name='platoon')
    game_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='gameId')
    player_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='playerId')


class GameStatusInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    possession = sgqlc.types.Field(sgqlc.types.non_null(Possession), graphql_name='possession')
    quarter = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quarter')
    yards_to_go = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yardsToGo')
    down = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='down')
    play_direction = sgqlc.types.Field(PrincipalWind, graphql_name='playDirection')
    yard_line = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yardLine')
    play_is_under_review = sgqlc.types.Field(Boolean, graphql_name='playIsUnderReview')
    game_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='gameId')
    yard_line_team = sgqlc.types.Field(sgqlc.types.non_null(YardLineTeam), graphql_name='yardLineTeam')
    home_team_timeouts_remaining = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='homeTeamTimeoutsRemaining')
    home_team_points_by_quarter = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='homeTeamPointsByQuarter')
    away_team_points_by_quarter = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='awayTeamPointsByQuarter')
    away_team_timeouts_remaining = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='awayTeamTimeoutsRemaining')
    phase = sgqlc.types.Field(sgqlc.types.non_null(GamePhase), graphql_name='phase')
    time = sgqlc.types.Field(DateTime, graphql_name='time')


class NamedTimeRangeInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='time')
    duration_milliseconds = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='durationMilliseconds')
    season_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='seasonId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class NamedTimeRangePatchInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    name = sgqlc.types.Field(String, graphql_name='name')
    time = sgqlc.types.Field(DateTime, graphql_name='time')
    subseason = sgqlc.types.Field(Subseason, graphql_name='subseason')


class OfficialInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    weight_grams = sgqlc.types.Field(Int, graphql_name='weightGrams')
    biography = sgqlc.types.Field(String, graphql_name='biography')
    personnel_notes = sgqlc.types.Field(String, graphql_name='personnelNotes')
    avatar_file_id = sgqlc.types.Field(ID, graphql_name='avatarFileId')
    legal_name = sgqlc.types.Field('PersonNameInput', graphql_name='legalName')
    common_name = sgqlc.types.Field('PersonNameInput', graphql_name='commonName')
    birth_date = sgqlc.types.Field(Date, graphql_name='birthDate')
    height_millimeters = sgqlc.types.Field(Int, graphql_name='heightMillimeters')


class OfficialPatchInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    birth_date = sgqlc.types.Field(Date, graphql_name='birthDate')
    height_millimeters = sgqlc.types.Field(Int, graphql_name='heightMillimeters')
    weight_grams = sgqlc.types.Field(Int, graphql_name='weightGrams')
    biography = sgqlc.types.Field(String, graphql_name='biography')
    personnel_notes = sgqlc.types.Field(String, graphql_name='personnelNotes')
    avatar_file_id = sgqlc.types.Field(ID, graphql_name='avatarFileId')
    legal_name = sgqlc.types.Field('PersonNameInput', graphql_name='legalName')
    common_name = sgqlc.types.Field('PersonNameInput', graphql_name='commonName')


class PersonNameInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    family_name_pronunciation = sgqlc.types.Field(String, graphql_name='familyNamePronunciation')
    given_name = sgqlc.types.Field(String, graphql_name='givenName')
    middle_name = sgqlc.types.Field(String, graphql_name='middleName')
    family_name = sgqlc.types.Field(String, graphql_name='familyName')
    suffix = sgqlc.types.Field(String, graphql_name='suffix')
    given_name_pronunciation = sgqlc.types.Field(String, graphql_name='givenNamePronunciation')


class PersonTelemetrySampleInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    time = sgqlc.types.Field(DateTime, graphql_name='time')
    position_meters = sgqlc.types.Field('Point3DInput', graphql_name='positionMeters')
    orientation = sgqlc.types.Field('QuaternionInput', graphql_name='orientation')
    person_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='personId')


class PlayInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    time = sgqlc.types.Field(DateTime, graphql_name='time')
    is_conversion = sgqlc.types.Field(Boolean, graphql_name='isConversion')
    game_clock_seconds = sgqlc.types.Field(Int, graphql_name='gameClockSeconds')
    direction = sgqlc.types.Field(PrincipalWind, graphql_name='direction')
    duration_milliseconds = sgqlc.types.Field(Int, graphql_name='durationMilliseconds')
    type = sgqlc.types.Field(PlayType, graphql_name='type')
    yard_line_team = sgqlc.types.Field(sgqlc.types.non_null(YardLineTeam), graphql_name='yardLineTeam')
    game_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='gameId')
    description = sgqlc.types.Field(String, graphql_name='description')
    yards_to_go = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yardsToGo')
    down = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='down')
    possession = sgqlc.types.Field(sgqlc.types.non_null(Possession), graphql_name='possession')
    yard_line = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yardLine')
    no_play = sgqlc.types.Field(Boolean, graphql_name='noPlay')
    quarter = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quarter')
    is_complete = sgqlc.types.Field(Boolean, graphql_name='isComplete')


class PlayPatchInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    type = sgqlc.types.Field(PlayType, graphql_name='type')
    is_complete = sgqlc.types.Field(Boolean, graphql_name='isComplete')
    sequence = sgqlc.types.Field(Float, graphql_name='sequence')
    time = sgqlc.types.Field(DateTime, graphql_name='time')
    description = sgqlc.types.Field(String, graphql_name='description')
    game_clock_seconds = sgqlc.types.Field(Int, graphql_name='gameClockSeconds')
    has_injury = sgqlc.types.Field(Boolean, graphql_name='hasInjury')
    duration_milliseconds = sgqlc.types.Field(Int, graphql_name='durationMilliseconds')
    no_play = sgqlc.types.Field(Boolean, graphql_name='noPlay')
    has_penalty = sgqlc.types.Field(Boolean, graphql_name='hasPenalty')


class PlayerInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    email_address = sgqlc.types.Field(String, graphql_name='emailAddress')
    depth = sgqlc.types.Field(Int, graphql_name='depth')
    weight_grams = sgqlc.types.Field(Int, graphql_name='weightGrams')
    tender_date = sgqlc.types.Field(Date, graphql_name='tenderDate')
    schools = sgqlc.types.Field(sgqlc.types.list_of('PlayerSchoolInput'), graphql_name='schools')
    phone_number = sgqlc.types.Field(String, graphql_name='phoneNumber')
    hometown = sgqlc.types.Field(AddressInput, graphql_name='hometown')
    height_millimeters = sgqlc.types.Field(Int, graphql_name='heightMillimeters')
    jersey_number = sgqlc.types.Field(Int, graphql_name='jerseyNumber')
    nfl_status = sgqlc.types.Field('PlayerLeagueStatusInput', graphql_name='nflStatus')
    avatar_file_id = sgqlc.types.Field(ID, graphql_name='avatarFileId')
    biography = sgqlc.types.Field(String, graphql_name='biography')
    team_id = sgqlc.types.Field(ID, graphql_name='teamId')
    position = sgqlc.types.Field(PlayerPosition, graphql_name='position')
    personnel_notes = sgqlc.types.Field(String, graphql_name='personnelNotes')
    is_allocated = sgqlc.types.Field(Boolean, graphql_name='isAllocated')
    birth_date = sgqlc.types.Field(Date, graphql_name='birthDate')
    cfl_status = sgqlc.types.Field('PlayerLeagueStatusInput', graphql_name='cflStatus')
    legal_name = sgqlc.types.Field(PersonNameInput, graphql_name='legalName')
    common_name = sgqlc.types.Field(PersonNameInput, graphql_name='commonName')
    agent_id = sgqlc.types.Field(ID, graphql_name='agentId')


class PlayerLeagueStatusInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    date = sgqlc.types.Field(Date, graphql_name='date')
    team = sgqlc.types.Field(String, graphql_name='team')
    jersey_number = sgqlc.types.Field(Int, graphql_name='jerseyNumber')
    status = sgqlc.types.Field(String, graphql_name='status')


class PlayerPatchInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    avatar_file_id = sgqlc.types.Field(ID, graphql_name='avatarFileId')
    jersey_number = sgqlc.types.Field(Int, graphql_name='jerseyNumber')
    agent_id = sgqlc.types.Field(ID, graphql_name='agentId')
    schools = sgqlc.types.Field(sgqlc.types.list_of('PlayerSchoolInput'), graphql_name='schools')
    weight_grams = sgqlc.types.Field(Int, graphql_name='weightGrams')
    hometown = sgqlc.types.Field(AddressInput, graphql_name='hometown')
    legal_name = sgqlc.types.Field(PersonNameInput, graphql_name='legalName')
    birth_date = sgqlc.types.Field(Date, graphql_name='birthDate')
    is_allocated = sgqlc.types.Field(Boolean, graphql_name='isAllocated')
    nfl_status = sgqlc.types.Field(PlayerLeagueStatusInput, graphql_name='nflStatus')
    cfl_status = sgqlc.types.Field(PlayerLeagueStatusInput, graphql_name='cflStatus')
    tender_date = sgqlc.types.Field(Date, graphql_name='tenderDate')
    phone_number = sgqlc.types.Field(String, graphql_name='phoneNumber')
    career_summary = sgqlc.types.Field(String, graphql_name='careerSummary')
    height_millimeters = sgqlc.types.Field(Int, graphql_name='heightMillimeters')
    common_name = sgqlc.types.Field(PersonNameInput, graphql_name='commonName')
    biography = sgqlc.types.Field(String, graphql_name='biography')
    personnel_notes = sgqlc.types.Field(String, graphql_name='personnelNotes')
    depth = sgqlc.types.Field(Int, graphql_name='depth')
    community_activities_summary = sgqlc.types.Field(String, graphql_name='communityActivitiesSummary')
    email_address = sgqlc.types.Field(String, graphql_name='emailAddress')
    sportradar_ncaafbid = sgqlc.types.Field(String, graphql_name='sportradarNCAAFBId')
    position = sgqlc.types.Field(PlayerPosition, graphql_name='position')
    team_id = sgqlc.types.Field(ID, graphql_name='teamId')


class PlayerSchoolInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    jersey_number = sgqlc.types.Field(Int, graphql_name='jerseyNumber')
    start_date = sgqlc.types.Field(Date, graphql_name='startDate')
    end_date = sgqlc.types.Field(Date, graphql_name='endDate')
    school_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='schoolId')


class PlayerTransactionInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    waiver_deadline = sgqlc.types.Field(DateTime, graphql_name='waiverDeadline')
    player_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='playerId')
    team_id = sgqlc.types.Field(ID, graphql_name='teamId')
    date = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='date')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    roster_status = sgqlc.types.Field(sgqlc.types.non_null(PlayerRosterStatus), graphql_name='rosterStatus')


class Point3DInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    x = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='x')
    y = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='y')
    z = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='z')


class QuaternionInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    y = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='y')
    z = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='z')
    w = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='w')
    x = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='x')


class SchoolInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    abbreviation = sgqlc.types.Field(String, graphql_name='abbreviation')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    is_ncaa = sgqlc.types.Field(Boolean, graphql_name='isNCAA')


class SchoolPatchInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    name = sgqlc.types.Field(String, graphql_name='name')
    is_ncaa = sgqlc.types.Field(Boolean, graphql_name='isNCAA')
    abbreviation = sgqlc.types.Field(String, graphql_name='abbreviation')


class SeasonInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    year = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='year')


class SeasonPatchInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    year = sgqlc.types.Field(Int, graphql_name='year')


class StadiumInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    address = sgqlc.types.Field(AddressInput, graphql_name='address')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class StadiumPatchInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    name = sgqlc.types.Field(String, graphql_name='name')
    address = sgqlc.types.Field(AddressInput, graphql_name='address')


class TeamInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    region_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='regionName')
    nickname = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nickname')
    abbreviation = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='abbreviation')
    stadium_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='stadiumId')


class TeamPatchInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    instagram_handle = sgqlc.types.Field(String, graphql_name='instagramHandle')
    shop_website_url = sgqlc.types.Field(String, graphql_name='shopWebsiteURL')
    abbreviation = sgqlc.types.Field(String, graphql_name='abbreviation')
    background_banner_dark_file_id = sgqlc.types.Field(ID, graphql_name='backgroundBannerDarkFileId')
    avatar_file_id = sgqlc.types.Field(ID, graphql_name='avatarFileId')
    ticketing_website_url = sgqlc.types.Field(String, graphql_name='ticketingWebsiteURL')
    stadium_id = sgqlc.types.Field(ID, graphql_name='stadiumId')
    twitter_handle = sgqlc.types.Field(String, graphql_name='twitterHandle')
    wordmark_light_background_file_id = sgqlc.types.Field(ID, graphql_name='wordmarkLightBackgroundFileId')
    website_url = sgqlc.types.Field(String, graphql_name='websiteURL')
    division_id = sgqlc.types.Field(ID, graphql_name='divisionId')
    wordmark_file_id = sgqlc.types.Field(ID, graphql_name='wordmarkFileId')
    region_name = sgqlc.types.Field(String, graphql_name='regionName')
    colors = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Color)), graphql_name='colors')
    nickname = sgqlc.types.Field(String, graphql_name='nickname')
    logo_file_id = sgqlc.types.Field(ID, graphql_name='logoFileId')
    facebook_handle = sgqlc.types.Field(String, graphql_name='facebookHandle')
    logo_light_background_file_id = sgqlc.types.Field(ID, graphql_name='logoLightBackgroundFileId')


class UserLevelInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')
    required_xp = sgqlc.types.Field(sgqlc.types.non_null(LongInt), graphql_name='requiredXP')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')


class UserLevelPatchInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    required_xp = sgqlc.types.Field(LongInt, graphql_name='requiredXP')
    title = sgqlc.types.Field(String, graphql_name='title')
    number = sgqlc.types.Field(Int, graphql_name='number')


class UserPatchInput(sgqlc.types.Input):
    __schema__ = aaf_schema
    handle = sgqlc.types.Field(String, graphql_name='handle')
    avatar_file_id = sgqlc.types.Field(ID, graphql_name='avatarFileId')
    roles = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(UserRole)), graphql_name='roles')
    email_address = sgqlc.types.Field(String, graphql_name='emailAddress')
    phone_number = sgqlc.types.Field(String, graphql_name='phoneNumber')



########################################################################
# Output Objects and Interfaces
########################################################################
class AVProgramAVStreamEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('AVStream'), graphql_name='node')


class AVProgramAVStreamsConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(AVProgramAVStreamEdge)), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('AVStream')), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class AVStreamAVStreamSegmentReplicaEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('AVStreamSegmentReplica'), graphql_name='node')


class AVStreamAVStreamSegmentReplicasConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(AVStreamAVStreamSegmentReplicaEdge)), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('AVStreamSegmentReplica')), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class Address(sgqlc.types.Type):
    __schema__ = aaf_schema
    administrative_area = sgqlc.types.Field(String, graphql_name='administrativeArea')
    administrative_area_abbreviation = sgqlc.types.Field(String, graphql_name='administrativeAreaAbbreviation')
    country_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='countryCode')
    line1 = sgqlc.types.Field(String, graphql_name='line1')
    line2 = sgqlc.types.Field(String, graphql_name='line2')
    locality = sgqlc.types.Field(String, graphql_name='locality')
    postal_code = sgqlc.types.Field(String, graphql_name='postalCode')


class AgentEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Agent'), graphql_name='node')


class AgentsConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(AgentEdge)), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Agent')), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class AggregatedTeamStats(sgqlc.types.Type):
    __schema__ = aaf_schema
    average_passing_yards_net_per_game = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='averagePassingYardsNetPerGame')
    average_points_per_game = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='averagePointsPerGame')
    average_rushing_yards_net_per_game = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='averageRushingYardsNetPerGame')
    average_time_of_possession_per_game_milliseconds = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='averageTimeOfPossessionPerGameMilliseconds')
    average_times_sacked_per_game = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='averageTimesSackedPerGame')
    average_turnovers_per_game = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='averageTurnoversPerGame')
    average_yards_per_play = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='averageYardsPerPlay')
    field_goals_attempted = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fieldGoalsAttempted')
    field_goals_blocked = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fieldGoalsBlocked')
    field_goals_made = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fieldGoalsMade')
    first_downs_by_passing = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='firstDownsByPassing')
    first_downs_by_penalty = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='firstDownsByPenalty')
    first_downs_by_rushing = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='firstDownsByRushing')
    fourth_downs_converted = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fourthDownsConverted')
    fourth_downs_unconverted = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fourthDownsUnconverted')
    fumbles = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fumbles')
    games_lost = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='gamesLost')
    games_played = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='gamesPlayed')
    games_won = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='gamesWon')
    interception_return_yards = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='interceptionReturnYards')
    interception_returns = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='interceptionReturns')
    own_fumbles_recovered = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='ownFumblesRecovered')
    passes_attempted = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='passesAttempted')
    passes_completed = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='passesCompleted')
    passes_intercepted = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='passesIntercepted')
    passing_plays = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='passingPlays')
    passing_yards_gross = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='passingYardsGross')
    passing_yards_net = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='passingYardsNet')
    points = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='points')
    rushing_plays = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rushingPlays')
    rushing_yards_net = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rushingYardsNet')
    sack_yards_lost = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='sackYardsLost')
    safeties = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='safeties')
    third_downs_converted = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='thirdDownsConverted')
    third_downs_unconverted = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='thirdDownsUnconverted')
    time_of_possession_milliseconds = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='timeOfPossessionMilliseconds')
    times_sacked = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='timesSacked')
    touchdowns = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='touchdowns')
    turnovers = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='turnovers')
    two_point_conversion_completion_percentage = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='twoPointConversionCompletionPercentage')
    two_point_conversions_attempted = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='twoPointConversionsAttempted')
    two_point_conversions_completed = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='twoPointConversionsCompleted')


class BallBallTelemetrySampleConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('BallBallTelemetrySampleEdge')), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('BallTelemetrySample')), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class BallBallTelemetrySampleEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('BallTelemetrySample'), graphql_name='node')


class BallGameEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Game'), graphql_name='node')


class BallGamesConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(BallGameEdge)), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Game')), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class BallTelemetrySamplesSubscriptionData(sgqlc.types.Type):
    __schema__ = aaf_schema
    samples = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('BallTelemetrySample')), graphql_name='samples')


class CoinToss(sgqlc.types.Type):
    __schema__ = aaf_schema
    before_quarter = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='beforeQuarter')
    losing_choice = sgqlc.types.Field('CoinTossChoice', graphql_name='losingChoice')
    winning_choice = sgqlc.types.Field('CoinTossChoice', graphql_name='winningChoice')
    winning_team = sgqlc.types.Field('Team', graphql_name='winningTeam')


class CoinTossChoice(sgqlc.types.Type):
    __schema__ = aaf_schema
    direction = sgqlc.types.Field(PrincipalWind, graphql_name='direction')
    option = sgqlc.types.Field(sgqlc.types.non_null(CoinTossChoiceOption), graphql_name='option')


class CompleteU2FDeviceRegistrationResult(sgqlc.types.Type):
    __schema__ = aaf_schema
    device = sgqlc.types.Field(sgqlc.types.non_null('U2FDevice'), graphql_name='device')


class CompleteU2FDeviceVerificationResult(sgqlc.types.Type):
    __schema__ = aaf_schema
    access_token = sgqlc.types.Field(sgqlc.types.non_null('AccessToken'), graphql_name='accessToken')
    secret = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='secret')


class CreateAccessTokenResult(sgqlc.types.Type):
    __schema__ = aaf_schema
    access_token = sgqlc.types.Field(sgqlc.types.non_null('AccessToken'), graphql_name='accessToken')
    secret = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='secret')


class CreateAnonymousUserResult(sgqlc.types.Type):
    __schema__ = aaf_schema
    secret = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='secret')
    user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='user')


class CreateBallTelemetrySamplesResult(sgqlc.types.Type):
    __schema__ = aaf_schema
    samples = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('BallTelemetrySample'))), graphql_name='samples')


class CreatePersonTelemetrySamplesResult(sgqlc.types.Type):
    __schema__ = aaf_schema
    samples = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PersonTelemetrySample'))), graphql_name='samples')


class DepthChart(sgqlc.types.Type):
    __schema__ = aaf_schema
    formations = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('DepthChartFormation')), graphql_name='formations')


class DepthChartFormation(sgqlc.types.Type):
    __schema__ = aaf_schema
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    players_connection = sgqlc.types.Field('DepthChartFormationPlayersConnection', graphql_name='playersConnection', args=sgqlc.types.ArgDict((
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )


class DepthChartFormationPlayerEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    depth = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='depth')
    node = sgqlc.types.Field(sgqlc.types.non_null('Player'), graphql_name='node')


class DepthChartFormationPlayersConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(DepthChartFormationPlayerEdge)), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Player')), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class EventAvailability(sgqlc.types.Type):
    __schema__ = aaf_schema
    logo = sgqlc.types.Field('File', graphql_name='logo')
    short_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='shortName')
    url = sgqlc.types.Field(String, graphql_name='url')


class EventEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Event'), graphql_name='node')


class EventsConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(EventEdge)), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Event')), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class FrontEndPreference(sgqlc.types.Type):
    __schema__ = aaf_schema
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    namespace = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='namespace')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class GameAVProgramEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('AVProgram'), graphql_name='node')


class GameAVProgramsConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(GameAVProgramEdge)), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('AVProgram')), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class GameBallEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Ball'), graphql_name='node')


class GameBallsConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(GameBallEdge)), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Ball')), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class GameClock(sgqlc.types.Type):
    __schema__ = aaf_schema
    seconds = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='seconds')
    time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='time')


class GameClockEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(GameClock), graphql_name='node')


class GameClockHistoryConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(GameClockEdge)), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(GameClock)), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class GameEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Game'), graphql_name='node')


class GameOfficialEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Official'), graphql_name='node')
    position = sgqlc.types.Field(OfficialPosition, graphql_name='position')


class GameOfficialsConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(GameOfficialEdge)), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Official')), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class GamePlayClock(sgqlc.types.Type):
    __schema__ = aaf_schema
    seconds = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='seconds')
    time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='time')


class GamePlayClockEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(GamePlayClock), graphql_name='node')


class GamePlayClockHistoryConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(GamePlayClockEdge)), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(GamePlayClock)), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class GamePlayEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Play'), graphql_name='node')


class GamePlayerEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    active = sgqlc.types.Field(Boolean, graphql_name='active')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    jersey_number = sgqlc.types.Field(Int, graphql_name='jerseyNumber')
    node = sgqlc.types.Field(sgqlc.types.non_null('Player'), graphql_name='node')
    played = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='played')
    position = sgqlc.types.Field(PlayerPosition, graphql_name='position')
    starter = sgqlc.types.Field(Boolean, graphql_name='starter')
    stats = sgqlc.types.Field('PlayerStats', graphql_name='stats')
    team = sgqlc.types.Field('Team', graphql_name='team')


class GamePlayersConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(GamePlayerEdge)), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Player')), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class GamePlaysConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(GamePlayEdge)), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Play')), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class GameStatus(sgqlc.types.Type):
    __schema__ = aaf_schema
    away_team_points = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='awayTeamPoints')
    away_team_points_by_quarter = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='awayTeamPointsByQuarter')
    away_team_timeouts_remaining = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='awayTeamTimeoutsRemaining')
    down = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='down')
    home_team_points = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='homeTeamPoints')
    home_team_points_by_quarter = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='homeTeamPointsByQuarter')
    home_team_timeouts_remaining = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='homeTeamTimeoutsRemaining')
    phase = sgqlc.types.Field(GamePhase, graphql_name='phase')
    play_direction = sgqlc.types.Field(PrincipalWind, graphql_name='playDirection')
    play_is_under_review = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='playIsUnderReview')
    possession = sgqlc.types.Field(Possession, graphql_name='possession')
    quarter = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quarter')
    time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='time')
    yard_line = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yardLine')
    yard_line_team = sgqlc.types.Field(YardLineTeam, graphql_name='yardLineTeam')
    yards_to_go = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yardsToGo')


class GameStatusEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(GameStatus), graphql_name='node')


class GameStatusHistoryConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(GameStatusEdge)), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(GameStatus)), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class GameTeamEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    depth_chart = sgqlc.types.Field(DepthChart, graphql_name='depthChart', args=sgqlc.types.ArgDict((
        ('platoon', sgqlc.types.Arg(sgqlc.types.non_null(Platoon), graphql_name='platoon', default=None)),
))
    )
    node = sgqlc.types.Field(sgqlc.types.non_null('Team'), graphql_name='node')
    stats = sgqlc.types.Field('TeamStats', graphql_name='stats')


class GameTimeoutEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Timeout'), graphql_name='node')


class GameTimeoutsConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(GameTimeoutEdge)), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Timeout')), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class GamesConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(GameEdge)), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Game')), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class Mutation(sgqlc.types.Type):
    __schema__ = aaf_schema
    add_game_ball = sgqlc.types.Field(Boolean, graphql_name='addGameBall', args=sgqlc.types.ArgDict((
        ('game_ball', sgqlc.types.Arg(sgqlc.types.non_null(GameBallInput), graphql_name='gameBall', default=None)),
))
    )
    add_game_player_formation_depth = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='addGamePlayerFormationDepth', args=sgqlc.types.ArgDict((
        ('game_player_formation_depth', sgqlc.types.Arg(sgqlc.types.non_null(GamePlayerFormationDepthInput), graphql_name='gamePlayerFormationDepth', default=None)),
))
    )
    add_user_avatar = sgqlc.types.Field(Boolean, graphql_name='addUserAvatar', args=sgqlc.types.ArgDict((
        ('file_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='fileId', default=None)),
))
    )
    complete_u2_fdevice_registration = sgqlc.types.Field(CompleteU2FDeviceRegistrationResult, graphql_name='completeU2FDeviceRegistration', args=sgqlc.types.ArgDict((
        ('client_data_base64', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='clientDataBase64', default=None)),
        ('registration_data_base64', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='registrationDataBase64', default=None)),
        ('version', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='version', default=None)),
))
    )
    complete_u2_fdevice_verification = sgqlc.types.Field(CompleteU2FDeviceVerificationResult, graphql_name='completeU2FDeviceVerification', args=sgqlc.types.ArgDict((
        ('key_handle_base64', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='keyHandleBase64', default=None)),
        ('client_data_base64', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='clientDataBase64', default=None)),
        ('signature_data_base64', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='signatureDataBase64', default=None)),
))
    )
    complete_user_password_reset = sgqlc.types.Field('User', graphql_name='completeUserPasswordReset', args=sgqlc.types.ArgDict((
        ('password', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='password', default=None)),
        ('token', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='token', default=None)),
))
    )
    create_avprogram = sgqlc.types.Field('AVProgram', graphql_name='createAVProgram', args=sgqlc.types.ArgDict((
        ('program', sgqlc.types.Arg(sgqlc.types.non_null(AVProgramInput), graphql_name='program', default=None)),
))
    )
    create_avstream = sgqlc.types.Field('AVStream', graphql_name='createAVStream', args=sgqlc.types.ArgDict((
        ('stream', sgqlc.types.Arg(sgqlc.types.non_null(AVStreamInput), graphql_name='stream', default=None)),
))
    )
    create_avstream_segment_replica = sgqlc.types.Field('AVStreamSegmentReplica', graphql_name='createAVStreamSegmentReplica', args=sgqlc.types.ArgDict((
        ('replica', sgqlc.types.Arg(sgqlc.types.non_null(AVStreamSegmentReplicaInput), graphql_name='replica', default=None)),
))
    )
    create_access_token = sgqlc.types.Field(CreateAccessTokenResult, graphql_name='createAccessToken', args=sgqlc.types.ArgDict((
        ('password', sgqlc.types.Arg(String, graphql_name='password', default=None)),
        ('lifespan_seconds', sgqlc.types.Arg(Int, graphql_name='lifespanSeconds', default=None)),
        ('human_readable', sgqlc.types.Arg(Boolean, graphql_name='humanReadable', default=None)),
        ('bearer_token', sgqlc.types.Arg(String, graphql_name='bearerToken', default=None)),
        ('email_address', sgqlc.types.Arg(String, graphql_name='emailAddress', default=None)),
))
    )
    create_agent = sgqlc.types.Field('Agent', graphql_name='createAgent', args=sgqlc.types.ArgDict((
        ('agent', sgqlc.types.Arg(sgqlc.types.non_null(AgentInput), graphql_name='agent', default=None)),
))
    )
    create_anonymous_user = sgqlc.types.Field(CreateAnonymousUserResult, graphql_name='createAnonymousUser')
    create_ball = sgqlc.types.Field('Ball', graphql_name='createBall')
    create_ball_telemetry_samples = sgqlc.types.Field(CreateBallTelemetrySamplesResult, graphql_name='createBallTelemetrySamples', args=sgqlc.types.ArgDict((
        ('game_id', sgqlc.types.Arg(ID, graphql_name='gameId', default=None)),
        ('samples', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BallTelemetrySampleInput))), graphql_name='samples', default=None)),
))
    )
    create_coach = sgqlc.types.Field('Player', graphql_name='createCoach', args=sgqlc.types.ArgDict((
        ('coach', sgqlc.types.Arg(sgqlc.types.non_null(CoachInput), graphql_name='coach', default=None)),
))
    )
    create_division = sgqlc.types.Field('Division', graphql_name='createDivision', args=sgqlc.types.ArgDict((
        ('division', sgqlc.types.Arg(sgqlc.types.non_null(DivisionInput), graphql_name='division', default=None)),
))
    )
    create_game = sgqlc.types.Field('Game', graphql_name='createGame', args=sgqlc.types.ArgDict((
        ('game', sgqlc.types.Arg(sgqlc.types.non_null(GameInput), graphql_name='game', default=None)),
))
    )
    create_named_time_range = sgqlc.types.Field('NamedTimeRange', graphql_name='createNamedTimeRange', args=sgqlc.types.ArgDict((
        ('named_time_range', sgqlc.types.Arg(sgqlc.types.non_null(NamedTimeRangeInput), graphql_name='namedTimeRange', default=None)),
))
    )
    create_official = sgqlc.types.Field('Official', graphql_name='createOfficial', args=sgqlc.types.ArgDict((
        ('official', sgqlc.types.Arg(sgqlc.types.non_null(OfficialInput), graphql_name='official', default=None)),
))
    )
    create_person_telemetry_samples = sgqlc.types.Field(CreatePersonTelemetrySamplesResult, graphql_name='createPersonTelemetrySamples', args=sgqlc.types.ArgDict((
        ('game_id', sgqlc.types.Arg(ID, graphql_name='gameId', default=None)),
        ('samples', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PersonTelemetrySampleInput))), graphql_name='samples', default=None)),
))
    )
    create_play = sgqlc.types.Field('Play', graphql_name='createPlay', args=sgqlc.types.ArgDict((
        ('play', sgqlc.types.Arg(sgqlc.types.non_null(PlayInput), graphql_name='play', default=None)),
))
    )
    create_player = sgqlc.types.Field('Player', graphql_name='createPlayer', args=sgqlc.types.ArgDict((
        ('player', sgqlc.types.Arg(sgqlc.types.non_null(PlayerInput), graphql_name='player', default=None)),
))
    )
    create_player_transaction = sgqlc.types.Field('PlayerTransaction', graphql_name='createPlayerTransaction', args=sgqlc.types.ArgDict((
        ('transaction', sgqlc.types.Arg(sgqlc.types.non_null(PlayerTransactionInput), graphql_name='transaction', default=None)),
))
    )
    create_school = sgqlc.types.Field('School', graphql_name='createSchool', args=sgqlc.types.ArgDict((
        ('school', sgqlc.types.Arg(sgqlc.types.non_null(SchoolInput), graphql_name='school', default=None)),
))
    )
    create_season = sgqlc.types.Field('Season', graphql_name='createSeason', args=sgqlc.types.ArgDict((
        ('season', sgqlc.types.Arg(sgqlc.types.non_null(SeasonInput), graphql_name='season', default=None)),
))
    )
    create_stadium = sgqlc.types.Field('Stadium', graphql_name='createStadium', args=sgqlc.types.ArgDict((
        ('stadium', sgqlc.types.Arg(sgqlc.types.non_null(StadiumInput), graphql_name='stadium', default=None)),
))
    )
    create_team = sgqlc.types.Field('Team', graphql_name='createTeam', args=sgqlc.types.ArgDict((
        ('team', sgqlc.types.Arg(sgqlc.types.non_null(TeamInput), graphql_name='team', default=None)),
))
    )
    create_user = sgqlc.types.Field('User', graphql_name='createUser', args=sgqlc.types.ArgDict((
        ('email_address', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='emailAddress', default=None)),
        ('handle', sgqlc.types.Arg(String, graphql_name='handle', default=None)),
))
    )
    create_user_level = sgqlc.types.Field('UserLevel', graphql_name='createUserLevel', args=sgqlc.types.ArgDict((
        ('level', sgqlc.types.Arg(sgqlc.types.non_null(UserLevelInput), graphql_name='level', default=None)),
))
    )
    delete_avprogram = sgqlc.types.Field(Boolean, graphql_name='deleteAVProgram', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_avstream = sgqlc.types.Field(Boolean, graphql_name='deleteAVStream', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_access_token = sgqlc.types.Field(Boolean, graphql_name='deleteAccessToken', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_game = sgqlc.types.Field(Boolean, graphql_name='deleteGame', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_player_transaction = sgqlc.types.Field(Boolean, graphql_name='deletePlayerTransaction', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_user_level = sgqlc.types.Field(Boolean, graphql_name='deleteUserLevel', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_vod = sgqlc.types.Field(Boolean, graphql_name='deleteVOD', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    patch_avprogram = sgqlc.types.Field('AVProgram', graphql_name='patchAVProgram', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('patch', sgqlc.types.Arg(sgqlc.types.non_null(AVProgramPatchInput), graphql_name='patch', default=None)),
))
    )
    patch_avstream = sgqlc.types.Field('AVStream', graphql_name='patchAVStream', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('patch', sgqlc.types.Arg(sgqlc.types.non_null(AVStreamPatchInput), graphql_name='patch', default=None)),
))
    )
    patch_agent = sgqlc.types.Field('Agent', graphql_name='patchAgent', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('patch', sgqlc.types.Arg(sgqlc.types.non_null(AgentPatchInput), graphql_name='patch', default=None)),
))
    )
    patch_coach = sgqlc.types.Field('Coach', graphql_name='patchCoach', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('patch', sgqlc.types.Arg(sgqlc.types.non_null(CoachPatchInput), graphql_name='patch', default=None)),
))
    )
    patch_game = sgqlc.types.Field('Game', graphql_name='patchGame', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('patch', sgqlc.types.Arg(sgqlc.types.non_null(GamePatchInput), graphql_name='patch', default=None)),
))
    )
    patch_named_time_range = sgqlc.types.Field('NamedTimeRange', graphql_name='patchNamedTimeRange', args=sgqlc.types.ArgDict((
        ('patch', sgqlc.types.Arg(sgqlc.types.non_null(NamedTimeRangePatchInput), graphql_name='patch', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    patch_official = sgqlc.types.Field('Official', graphql_name='patchOfficial', args=sgqlc.types.ArgDict((
        ('patch', sgqlc.types.Arg(sgqlc.types.non_null(OfficialPatchInput), graphql_name='patch', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    patch_play = sgqlc.types.Field('Play', graphql_name='patchPlay', args=sgqlc.types.ArgDict((
        ('patch', sgqlc.types.Arg(sgqlc.types.non_null(PlayPatchInput), graphql_name='patch', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    patch_player = sgqlc.types.Field('Player', graphql_name='patchPlayer', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('patch', sgqlc.types.Arg(sgqlc.types.non_null(PlayerPatchInput), graphql_name='patch', default=None)),
))
    )
    patch_school = sgqlc.types.Field('School', graphql_name='patchSchool', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('patch', sgqlc.types.Arg(sgqlc.types.non_null(SchoolPatchInput), graphql_name='patch', default=None)),
))
    )
    patch_season = sgqlc.types.Field('Season', graphql_name='patchSeason', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('patch', sgqlc.types.Arg(sgqlc.types.non_null(SeasonPatchInput), graphql_name='patch', default=None)),
))
    )
    patch_stadium = sgqlc.types.Field('Stadium', graphql_name='patchStadium', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('patch', sgqlc.types.Arg(sgqlc.types.non_null(StadiumPatchInput), graphql_name='patch', default=None)),
))
    )
    patch_team = sgqlc.types.Field('Team', graphql_name='patchTeam', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('patch', sgqlc.types.Arg(sgqlc.types.non_null(TeamPatchInput), graphql_name='patch', default=None)),
))
    )
    patch_user = sgqlc.types.Field('User', graphql_name='patchUser', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('patch', sgqlc.types.Arg(sgqlc.types.non_null(UserPatchInput), graphql_name='patch', default=None)),
))
    )
    patch_user_level = sgqlc.types.Field('UserLevel', graphql_name='patchUserLevel', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('patch', sgqlc.types.Arg(sgqlc.types.non_null(UserLevelPatchInput), graphql_name='patch', default=None)),
))
    )
    put_game_official = sgqlc.types.Field(Boolean, graphql_name='putGameOfficial', args=sgqlc.types.ArgDict((
        ('official_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='officialId', default=None)),
        ('position', sgqlc.types.Arg(sgqlc.types.non_null(OfficialPosition), graphql_name='position', default=None)),
        ('game_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='gameId', default=None)),
))
    )
    redeem_user_token_code = sgqlc.types.Field('RedeemUserTokenCodeResult', graphql_name='redeemUserTokenCode', args=sgqlc.types.ArgDict((
        ('code_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='codeId', default=None)),
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
))
    )
    register_u2_fdevice = sgqlc.types.Field('RegisterU2FDeviceResult', graphql_name='registerU2FDevice')
    remove_game_official = sgqlc.types.Field(Boolean, graphql_name='removeGameOfficial', args=sgqlc.types.ArgDict((
        ('game_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='gameId', default=None)),
        ('official_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='officialId', default=None)),
))
    )
    remove_game_player_formation_depth = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='removeGamePlayerFormationDepth', args=sgqlc.types.ArgDict((
        ('game_player_formation_depth', sgqlc.types.Arg(sgqlc.types.non_null(GamePlayerFormationDepthInput), graphql_name='gamePlayerFormationDepth', default=None)),
))
    )
    remove_user_avatar = sgqlc.types.Field(Boolean, graphql_name='removeUserAvatar', args=sgqlc.types.ArgDict((
        ('file_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='fileId', default=None)),
))
    )
    reset_user_password = sgqlc.types.Field('ResetUserPasswordResult', graphql_name='resetUserPassword', args=sgqlc.types.ArgDict((
        ('email_address', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='emailAddress', default=None)),
))
    )
    set_game_clock = sgqlc.types.Field(Boolean, graphql_name='setGameClock', args=sgqlc.types.ArgDict((
        ('clock', sgqlc.types.Arg(sgqlc.types.non_null(GameClockInput), graphql_name='clock', default=None)),
))
    )
    set_game_play_clock = sgqlc.types.Field(Boolean, graphql_name='setGamePlayClock', args=sgqlc.types.ArgDict((
        ('clock', sgqlc.types.Arg(sgqlc.types.non_null(GamePlayClockInput), graphql_name='clock', default=None)),
))
    )
    set_game_status = sgqlc.types.Field(Boolean, graphql_name='setGameStatus', args=sgqlc.types.ArgDict((
        ('status', sgqlc.types.Arg(sgqlc.types.non_null(GameStatusInput), graphql_name='status', default=None)),
))
    )
    verify_u2_fdevice = sgqlc.types.Field('VerifyU2FDeviceResult', graphql_name='verifyU2FDevice')


class Node(sgqlc.types.Interface):
    __schema__ = aaf_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class OfficialEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Official'), graphql_name='node')


class OfficialsConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(OfficialEdge)), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Official')), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PageInfo(sgqlc.types.Type):
    __schema__ = aaf_schema
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')


class Person(sgqlc.types.Interface):
    __schema__ = aaf_schema
    common_name = sgqlc.types.Field('PersonName', graphql_name='commonName')
    height_millimeters = sgqlc.types.Field(Int, graphql_name='heightMillimeters')
    name = sgqlc.types.Field(sgqlc.types.non_null('PersonName'), graphql_name='name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    telemetry_samples_connection = sgqlc.types.Field('PersonPersonTelemetrySampleConnection', graphql_name='telemetrySamplesConnection')
    biography = sgqlc.types.Field(String, graphql_name='biography')
    legal_name = sgqlc.types.Field('PersonName', graphql_name='legalName')
    avatar = sgqlc.types.Field('File', graphql_name='avatar')
    birth_date = sgqlc.types.Field(Date, graphql_name='birthDate')
    personnel_notes = sgqlc.types.Field(String, graphql_name='personnelNotes')
    weight_grams = sgqlc.types.Field(Int, graphql_name='weightGrams')


class PersonName(sgqlc.types.Type):
    __schema__ = aaf_schema
    family_name = sgqlc.types.Field(String, graphql_name='familyName')
    family_name_pronunciation = sgqlc.types.Field(String, graphql_name='familyNamePronunciation')
    given_name = sgqlc.types.Field(String, graphql_name='givenName')
    given_name_pronunciation = sgqlc.types.Field(String, graphql_name='givenNamePronunciation')
    middle_name = sgqlc.types.Field(String, graphql_name='middleName')
    pronunciation = sgqlc.types.Field(String, graphql_name='pronunciation')
    suffix = sgqlc.types.Field(String, graphql_name='suffix')


class PersonPersonTelemetrySampleConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('PersonPersonTelemetrySampleEdge')), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('PersonTelemetrySample')), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class PersonPersonTelemetrySampleEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('PersonTelemetrySample'), graphql_name='node')


class PersonTelemetrySamplesSubscriptionData(sgqlc.types.Type):
    __schema__ = aaf_schema
    samples = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('PersonTelemetrySample')), graphql_name='samples')


class PlayStat(sgqlc.types.Type):
    __schema__ = aaf_schema
    is_nullified = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isNullified')
    player = sgqlc.types.Field('Player', graphql_name='player')
    subtype = sgqlc.types.Field(PlayStatSubtype, graphql_name='subtype')
    team = sgqlc.types.Field('Team', graphql_name='team')
    type = sgqlc.types.Field(sgqlc.types.non_null(PlayStatType), graphql_name='type')
    value = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='value')


class PlaySubscriptionData(sgqlc.types.Type):
    __schema__ = aaf_schema
    play = sgqlc.types.Field('Play', graphql_name='play')
    previous_revision = sgqlc.types.Field('Play', graphql_name='previousRevision')


class PlayerEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Player'), graphql_name='node')


class PlayerGameEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Game'), graphql_name='node')
    stats = sgqlc.types.Field('PlayerStats', graphql_name='stats')
    team = sgqlc.types.Field('Team', graphql_name='team')


class PlayerGamesConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(PlayerGameEdge)), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Game')), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class PlayerLeagueStatus(sgqlc.types.Type):
    __schema__ = aaf_schema
    date = sgqlc.types.Field(Date, graphql_name='date')
    jersey_number = sgqlc.types.Field(Int, graphql_name='jerseyNumber')
    status = sgqlc.types.Field(String, graphql_name='status')
    team = sgqlc.types.Field(String, graphql_name='team')


class PlayerNCAAFBCareer(sgqlc.types.Type):
    __schema__ = aaf_schema
    seasons = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PlayerNCAAFBCareerSeason'))), graphql_name='seasons')


class PlayerNCAAFBCareerSeason(sgqlc.types.Type):
    __schema__ = aaf_schema
    teams = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PlayerNCAAFBCareerSeasonTeam'))), graphql_name='teams')
    year = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='year')


class PlayerNCAAFBCareerSeasonTeam(sgqlc.types.Type):
    __schema__ = aaf_schema
    nickname = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nickname')
    region_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='regionName')
    stats = sgqlc.types.Field('PlayerNCAAFBStats', graphql_name='stats')


class PlayerNCAAFBStats(sgqlc.types.Type):
    __schema__ = aaf_schema
    field_goals_attempted = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fieldGoalsAttempted')
    field_goals_longest_made = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fieldGoalsLongestMade')
    field_goals_made = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fieldGoalsMade')
    fumble_recovery_touchdowns = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fumbleRecoveryTouchdowns')
    interception_return_touchdowns = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='interceptionReturnTouchdowns')
    interception_returns = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='interceptionReturns')
    non_offensive_touchdowns = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nonOffensiveTouchdowns')
    passes_attempted = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='passesAttempted')
    passes_completed = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='passesCompleted')
    passes_intercepted = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='passesIntercepted')
    passing_touchdowns = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='passingTouchdowns')
    passing_yards = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='passingYards')
    punting_inside20 = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='puntingInside20')
    punting_longest_kick = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='puntingLongestKick')
    punting_yards = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='puntingYards')
    punts_attempted = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='puntsAttempted')
    receiving_touchdowns = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='receivingTouchdowns')
    receiving_yards = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='receivingYards')
    receptions = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='receptions')
    rushes_attempted = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rushesAttempted')
    rushing_touchdowns = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rushingTouchdowns')
    rushing_yards = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rushingYards')
    sacks = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='sacks')
    tackles = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='tackles')


class PlayerPlayerTransactionEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('PlayerTransaction'), graphql_name='node')


class PlayerPlayerTransactionsConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(PlayerPlayerTransactionEdge)), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('PlayerTransaction')), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class PlayerSchoolEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    end_date = sgqlc.types.Field(Date, graphql_name='endDate')
    jersey_number = sgqlc.types.Field(Int, graphql_name='jerseyNumber')
    node = sgqlc.types.Field(sgqlc.types.non_null('School'), graphql_name='node')
    start_date = sgqlc.types.Field(Date, graphql_name='startDate')


class PlayerSchoolsConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(PlayerSchoolEdge)), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('School')), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class PlayerSeasonEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Season'), graphql_name='node')
    stats = sgqlc.types.Field('PlayerStats', graphql_name='stats')


class PlayerSeasonsConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(PlayerSeasonEdge)), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Season')), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class PlayerStats(sgqlc.types.Type):
    __schema__ = aaf_schema
    air_yards_attempted = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='airYardsAttempted')
    air_yards_completed = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='airYardsCompleted')
    air_yards_incomplete = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='airYardsIncomplete')
    assisted_tackles = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='assistedTackles')
    field_goals_attempted = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fieldGoalsAttempted')
    field_goals_blocked = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fieldGoalsBlocked')
    field_goals_longest_made = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fieldGoalsLongestMade')
    field_goals_made = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fieldGoalsMade')
    fumbles = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fumbles')
    fumbles_recovered = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fumblesRecovered')
    games_played = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='gamesPlayed')
    interception_returns = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='interceptionReturns')
    miscellaneous_assisted_tackles = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='miscellaneousAssistedTackles')
    miscellaneous_fumbles_recovered = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='miscellaneousFumblesRecovered')
    miscellaneous_opponent_fumbles_forced = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='miscellaneousOpponentFumblesForced')
    miscellaneous_opponent_fumbles_recovered = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='miscellaneousOpponentFumblesRecovered')
    miscellaneous_own_fumbles_recovered = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='miscellaneousOwnFumblesRecovered')
    miscellaneous_tackle_assists = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='miscellaneousTackleAssists')
    miscellaneous_tackles = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='miscellaneousTackles')
    opponent_fumbles_forced = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='opponentFumblesForced')
    opponent_fumbles_recovered = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='opponentFumblesRecovered')
    opposing_field_goals_blocked = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='opposingFieldGoalsBlocked')
    own_fumbles_recovered = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='ownFumblesRecovered')
    pass_defenses = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='passDefenses')
    pass_targets = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='passTargets')
    passes_attempted = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='passesAttempted')
    passes_completed = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='passesCompleted')
    passes_intercepted = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='passesIntercepted')
    passing_touchdowns = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='passingTouchdowns')
    passing_yards = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='passingYards')
    penalties = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='penalties')
    penalty_yards = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='penaltyYards')
    punting_longest_kick = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='puntingLongestKick')
    punting_yards = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='puntingYards')
    punting_yards_net = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='puntingYardsNet')
    punts_attempted = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='puntsAttempted')
    punts_inside20 = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='puntsInside20')
    punts_into_end_zone_without_touchbacks = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='puntsIntoEndZoneWithoutTouchbacks')
    punts_with_touchbacks = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='puntsWithTouchbacks')
    quarterback_hits = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quarterbackHits')
    receiving_longest_gain = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='receivingLongestGain')
    receiving_touchdowns = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='receivingTouchdowns')
    receiving_yards = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='receivingYards')
    receptions = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='receptions')
    rushes_attempted = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rushesAttempted')
    rushing_longest_gain = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rushingLongestGain')
    rushing_touchdowns = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rushingTouchdowns')
    rushing_yards = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rushingYards')
    sack_yards_gained = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='sackYardsGained')
    sack_yards_lost = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='sackYardsLost')
    sacks = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='sacks')
    special_teams_assisted_tackles = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='specialTeamsAssistedTackles')
    special_teams_fumbles_recovered = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='specialTeamsFumblesRecovered')
    special_teams_opponent_fumbles_forced = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='specialTeamsOpponentFumblesForced')
    special_teams_opponent_fumbles_recovered = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='specialTeamsOpponentFumblesRecovered')
    special_teams_own_fumbles_recovered = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='specialTeamsOwnFumblesRecovered')
    special_teams_tackle_assists = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='specialTeamsTackleAssists')
    special_teams_tackles = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='specialTeamsTackles')
    tackle_assists = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='tackleAssists')
    tackles = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='tackles')
    tackles_for_loss = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='tacklesForLoss')
    times_sacked = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='timesSacked')
    two_point_conversion_pass_receptions_good = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='twoPointConversionPassReceptionsGood')
    two_point_conversion_passes_good = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='twoPointConversionPassesGood')
    two_point_conversion_rushes_good = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='twoPointConversionRushesGood')
    two_point_conversions_completed = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='twoPointConversionsCompleted')
    yards_after_catches = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='yardsAfterCatches')


class PlayerTransactionEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('PlayerTransaction'), graphql_name='node')


class PlayerTransactionsConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(PlayerTransactionEdge)), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('PlayerTransaction')), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class PlayersConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(PlayerEdge)), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Player')), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class Point3D(sgqlc.types.Type):
    __schema__ = aaf_schema
    x = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='x')
    y = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='y')
    z = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='z')


class Quaternion(sgqlc.types.Type):
    __schema__ = aaf_schema
    w = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='w')
    x = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='x')
    y = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='y')
    z = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='z')


class Query(sgqlc.types.Type):
    __schema__ = aaf_schema
    access_token = sgqlc.types.Field('AccessToken', graphql_name='accessToken')
    agents_connection = sgqlc.types.Field(AgentsConnection, graphql_name='agentsConnection', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('autocomplete', sgqlc.types.Arg(String, graphql_name='autocomplete', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
))
    )
    effective_user_roles = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(UserRole))), graphql_name='effectiveUserRoles')
    games_connection = sgqlc.types.Field(GamesConnection, graphql_name='gamesConnection', args=sgqlc.types.ArgDict((
        ('before_time', sgqlc.types.Arg(DateTime, graphql_name='beforeTime', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('at_or_after_time', sgqlc.types.Arg(DateTime, graphql_name='atOrAfterTime', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    me = sgqlc.types.Field('User', graphql_name='me')
    node = sgqlc.types.Field(Node, graphql_name='node', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    officials_connection = sgqlc.types.Field(OfficialsConnection, graphql_name='officialsConnection', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    player_transactions_connection = sgqlc.types.Field(PlayerTransactionsConnection, graphql_name='playerTransactionsConnection', args=sgqlc.types.ArgDict((
        ('before_date', sgqlc.types.Arg(Date, graphql_name='beforeDate', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('at_or_after_date', sgqlc.types.Arg(Date, graphql_name='atOrAfterDate', default=None)),
))
    )
    players_connection = sgqlc.types.Field(PlayersConnection, graphql_name='playersConnection', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('platoon', sgqlc.types.Arg(Platoon, graphql_name='platoon', default=None)),
        ('position', sgqlc.types.Arg(PlayerPosition, graphql_name='position', default=None)),
        ('roster_status', sgqlc.types.Arg(PlayerRosterStatus, graphql_name='rosterStatus', default=None)),
        ('autocomplete', sgqlc.types.Arg(String, graphql_name='autocomplete', default=None)),
))
    )
    schools_connection = sgqlc.types.Field('SchoolsConnection', graphql_name='schoolsConnection', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('autocomplete', sgqlc.types.Arg(String, graphql_name='autocomplete', default=None)),
))
    )
    seasons_connection = sgqlc.types.Field('SeasonsConnection', graphql_name='seasonsConnection', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    sportradar_ncaafbplayer_search = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('SportradarNCAAFBPlayerSearchResult')), graphql_name='sportradarNCAAFBPlayerSearch', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    teams_connection = sgqlc.types.Field('TeamsConnection', graphql_name='teamsConnection', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    user = sgqlc.types.Field('User', graphql_name='user', args=sgqlc.types.ArgDict((
        ('handle', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='handle', default=None)),
))
    )
    user_avatars_connection = sgqlc.types.Field('UserAvatarsConnection', graphql_name='userAvatarsConnection', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    user_levels_connection = sgqlc.types.Field('UserLevelsConnection', graphql_name='userLevelsConnection', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )


class RedeemUserTokenCodeResult(sgqlc.types.Type):
    __schema__ = aaf_schema
    token = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='token')
    token_type = sgqlc.types.Field(sgqlc.types.non_null(UserTokenType), graphql_name='tokenType')


class RegisterU2FDeviceResult(sgqlc.types.Type):
    __schema__ = aaf_schema
    app_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='appId')
    challenge_base64 = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='challengeBase64')
    registered_devices = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('U2FDevice')), graphql_name='registeredDevices')


class ResetUserPasswordResult(sgqlc.types.Type):
    __schema__ = aaf_schema
    code_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='codeId')


class SchoolEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('School'), graphql_name='node')


class SchoolsConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(SchoolEdge)), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('School')), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SeasonEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Season'), graphql_name='node')


class SeasonGameEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Game'), graphql_name='node')


class SeasonGamesConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(SeasonGameEdge)), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Game')), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SeasonNamedTimeRangeEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('NamedTimeRange'), graphql_name='node')


class SeasonNamedTimeRangesConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(SeasonNamedTimeRangeEdge)), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('NamedTimeRange')), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class SeasonsConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(SeasonEdge)), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Season')), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class SportradarNCAAFBPlayerSearchResult(sgqlc.types.Type):
    __schema__ = aaf_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    teams = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SportradarNCAAFBPlayerSearchResultTeam'))), graphql_name='teams')


class SportradarNCAAFBPlayerSearchResultTeam(sgqlc.types.Type):
    __schema__ = aaf_schema
    jersey = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='jersey')
    market = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='market')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    position = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='position')
    year = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='year')


class Subscription(sgqlc.types.Type):
    __schema__ = aaf_schema
    ball_telemetry_samples = sgqlc.types.Field(BallTelemetrySamplesSubscriptionData, graphql_name='ballTelemetrySamples', args=sgqlc.types.ArgDict((
        ('game_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='gameId', default=None)),
))
    )
    game_clock = sgqlc.types.Field(GameClock, graphql_name='gameClock', args=sgqlc.types.ArgDict((
        ('game_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='gameId', default=None)),
))
    )
    game_play_clock = sgqlc.types.Field(GamePlayClock, graphql_name='gamePlayClock', args=sgqlc.types.ArgDict((
        ('game_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='gameId', default=None)),
))
    )
    game_status = sgqlc.types.Field(GameStatus, graphql_name='gameStatus', args=sgqlc.types.ArgDict((
        ('game_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='gameId', default=None)),
))
    )
    heartbeat = sgqlc.types.Field(DateTime, graphql_name='heartbeat')
    person_telemetry_samples = sgqlc.types.Field(PersonTelemetrySamplesSubscriptionData, graphql_name='personTelemetrySamples', args=sgqlc.types.ArgDict((
        ('game_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='gameId', default=None)),
))
    )
    plays = sgqlc.types.Field(PlaySubscriptionData, graphql_name='plays', args=sgqlc.types.ArgDict((
        ('game_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='gameId', default=None)),
))
    )
    timeouts = sgqlc.types.Field('TimeoutSubscriptionData', graphql_name='timeouts', args=sgqlc.types.ArgDict((
        ('game_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='gameId', default=None)),
))
    )
    user_xp = sgqlc.types.Field('UserXPSubscriptionData', graphql_name='userXP', args=sgqlc.types.ArgDict((
        ('user_id', sgqlc.types.Arg(ID, graphql_name='userId', default=None)),
))
    )


class TeamCoachEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Coach'), graphql_name='node')


class TeamCoachesConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(TeamCoachEdge)), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Coach')), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class TeamEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Team'), graphql_name='node')


class TeamGameEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Game'), graphql_name='node')
    stats = sgqlc.types.Field('TeamStats', graphql_name='stats')


class TeamGamesConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(TeamGameEdge)), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Game')), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class TeamPlayerEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Player'), graphql_name='node')


class TeamPlayersConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(TeamPlayerEdge)), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Player')), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TeamSeasonEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Season'), graphql_name='node')
    opposition_stats = sgqlc.types.Field('TeamStats', graphql_name='oppositionStats')
    standing = sgqlc.types.Field('TeamStanding', graphql_name='standing')
    stats = sgqlc.types.Field('TeamStats', graphql_name='stats')


class TeamSeasonsConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(TeamSeasonEdge)), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Season')), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class TeamStanding(sgqlc.types.Type):
    __schema__ = aaf_schema
    division_losses = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='divisionLosses')
    division_points = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='divisionPoints')
    division_points_allowed = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='divisionPointsAllowed')
    division_rank = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='divisionRank')
    division_ties = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='divisionTies')
    division_wins = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='divisionWins')
    losses = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='losses')
    points = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='points')
    points_allowed = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pointsAllowed')
    rank = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rank')
    ties = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='ties')
    touchdowns = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='touchdowns')
    touchdowns_allowed = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='touchdownsAllowed')
    wins = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='wins')


class TeamStats(sgqlc.types.Type):
    __schema__ = aaf_schema
    average_passing_yards_net_per_game = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='averagePassingYardsNetPerGame')
    average_points_per_game = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='averagePointsPerGame')
    average_rushing_yards_net_per_game = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='averageRushingYardsNetPerGame')
    average_time_of_possession_per_game_milliseconds = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='averageTimeOfPossessionPerGameMilliseconds')
    average_times_sacked_per_game = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='averageTimesSackedPerGame')
    average_turnovers_per_game = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='averageTurnoversPerGame')
    average_yards_per_play = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='averageYardsPerPlay')
    field_goals_attempted = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fieldGoalsAttempted')
    field_goals_blocked = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fieldGoalsBlocked')
    field_goals_made = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fieldGoalsMade')
    first_downs_by_passing = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='firstDownsByPassing')
    first_downs_by_penalty = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='firstDownsByPenalty')
    first_downs_by_rushing = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='firstDownsByRushing')
    fourth_downs_converted = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fourthDownsConverted')
    fourth_downs_unconverted = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fourthDownsUnconverted')
    fumbles = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fumbles')
    games_lost = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='gamesLost')
    games_played = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='gamesPlayed')
    games_won = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='gamesWon')
    interception_return_yards = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='interceptionReturnYards')
    interception_returns = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='interceptionReturns')
    own_fumbles_recovered = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='ownFumblesRecovered')
    passes_attempted = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='passesAttempted')
    passes_completed = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='passesCompleted')
    passes_intercepted = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='passesIntercepted')
    passing_plays = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='passingPlays')
    passing_yards_gross = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='passingYardsGross')
    passing_yards_net = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='passingYardsNet')
    penalties = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='penalties')
    penalty_yards = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='penaltyYards')
    points = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='points')
    rushing_plays = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rushingPlays')
    rushing_yards_net = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rushingYardsNet')
    sack_yards_lost = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='sackYardsLost')
    safeties = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='safeties')
    third_downs_converted = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='thirdDownsConverted')
    third_downs_unconverted = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='thirdDownsUnconverted')
    time_of_possession_milliseconds = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='timeOfPossessionMilliseconds')
    times_sacked = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='timesSacked')
    touchdowns = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='touchdowns')
    turnovers = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='turnovers')
    two_point_conversion_completion_percentage = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='twoPointConversionCompletionPercentage')
    two_point_conversions_attempted = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='twoPointConversionsAttempted')
    two_point_conversions_completed = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='twoPointConversionsCompleted')


class TeamsConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(TeamEdge)), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Team')), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TimeoutSubscriptionData(sgqlc.types.Type):
    __schema__ = aaf_schema
    previous_revision = sgqlc.types.Field('Timeout', graphql_name='previousRevision')
    timeout = sgqlc.types.Field('Timeout', graphql_name='timeout')


class UserAvatarEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('File'), graphql_name='node')


class UserAvatarsConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(UserAvatarEdge)), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('File')), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class UserLevelEdge(sgqlc.types.Type):
    __schema__ = aaf_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('UserLevel'), graphql_name='node')


class UserLevelsConnection(sgqlc.types.relay.Connection):
    __schema__ = aaf_schema
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(UserLevelEdge)), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('UserLevel')), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class UserXPSubscriptionData(sgqlc.types.Type):
    __schema__ = aaf_schema
    level = sgqlc.types.Field('UserLevel', graphql_name='level')
    level_before = sgqlc.types.Field('UserLevel', graphql_name='levelBefore')
    next_level = sgqlc.types.Field('UserLevel', graphql_name='nextLevel')
    xp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='xp')
    xp_before = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='xpBefore')


class VerifyU2FDeviceResult(sgqlc.types.Type):
    __schema__ = aaf_schema
    app_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='appId')
    challenge_base64 = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='challengeBase64')
    registered_devices = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('U2FDevice')), graphql_name='registeredDevices')


class AVProgram(sgqlc.types.Type, Node):
    __schema__ = aaf_schema
    av_streams_connection = sgqlc.types.Field(AVProgramAVStreamsConnection, graphql_name='avStreamsConnection', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    creation_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='creationTime')
    hls_master_playlist_url = sgqlc.types.Field(String, graphql_name='hlsMasterPlaylistURL')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_private = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPrivate')
    name = sgqlc.types.Field(String, graphql_name='name')
    thumbnail = sgqlc.types.Field('File', graphql_name='thumbnail')


class AVStream(sgqlc.types.Type, Node):
    __schema__ = aaf_schema
    av_stream_segment_replicas_connection = sgqlc.types.Field(AVStreamAVStreamSegmentReplicasConnection, graphql_name='avStreamSegmentReplicasConnection', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('at_or_after_time', sgqlc.types.Arg(DateTime, graphql_name='atOrAfterTime', default=None)),
        ('before_time', sgqlc.types.Arg(DateTime, graphql_name='beforeTime', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
))
    )
    bitrate = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='bitrate')
    codecs = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='codecs')
    creation_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='creationTime')
    hls_master_playlist_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='hlsMasterPlaylistURL')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_live = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isLive')
    maximum_segment_duration_milliseconds = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='maximumSegmentDurationMilliseconds')
    time_adjustment_milliseconds = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='timeAdjustmentMilliseconds')
    video_height = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='videoHeight')
    video_width = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='videoWidth')


class AVStreamSegmentReplica(sgqlc.types.Type, Node):
    __schema__ = aaf_schema
    creation_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='creationTime')
    discontinuity = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='discontinuity')
    duration_milliseconds = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='durationMilliseconds')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    segment_number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='segmentNumber')
    time = sgqlc.types.Field(DateTime, graphql_name='time')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')


class AccessToken(sgqlc.types.Type, Node):
    __schema__ = aaf_schema
    approximate_last_use_time = sgqlc.types.Field(DateTime, graphql_name='approximateLastUseTime')
    creation_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='creationTime')
    expiration_time = sgqlc.types.Field(DateTime, graphql_name='expirationTime')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    u2f_device = sgqlc.types.Field('U2FDevice', graphql_name='u2fDevice')
    user = sgqlc.types.Field('User', graphql_name='user')


class Agent(sgqlc.types.Type, Person, Node):
    __schema__ = aaf_schema
    avatar = sgqlc.types.Field('File', graphql_name='avatar')
    biography = sgqlc.types.Field(String, graphql_name='biography')
    birth_date = sgqlc.types.Field(Date, graphql_name='birthDate')
    common_name = sgqlc.types.Field(PersonName, graphql_name='commonName')
    email_address = sgqlc.types.Field(String, graphql_name='emailAddress')
    email_address_alternative = sgqlc.types.Field(String, graphql_name='emailAddressAlternative')
    height_millimeters = sgqlc.types.Field(Int, graphql_name='heightMillimeters')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    legal_name = sgqlc.types.Field(PersonName, graphql_name='legalName')
    name = sgqlc.types.Field(sgqlc.types.non_null(PersonName), graphql_name='name')
    personnel_notes = sgqlc.types.Field(String, graphql_name='personnelNotes')
    phone_number = sgqlc.types.Field(String, graphql_name='phoneNumber')
    phone_number_alternative = sgqlc.types.Field(String, graphql_name='phoneNumberAlternative')
    telemetry_samples_connection = sgqlc.types.Field(PersonPersonTelemetrySampleConnection, graphql_name='telemetrySamplesConnection', args=sgqlc.types.ArgDict((
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('at_or_after_time', sgqlc.types.Arg(DateTime, graphql_name='atOrAfterTime', default=None)),
        ('before_time', sgqlc.types.Arg(DateTime, graphql_name='beforeTime', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    weight_grams = sgqlc.types.Field(Int, graphql_name='weightGrams')


class Ball(sgqlc.types.Type, Node):
    __schema__ = aaf_schema
    games_connection = sgqlc.types.Field(BallGamesConnection, graphql_name='gamesConnection', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
))
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    telemetry_samples_connection = sgqlc.types.Field(BallBallTelemetrySampleConnection, graphql_name='telemetrySamplesConnection', args=sgqlc.types.ArgDict((
        ('before_time', sgqlc.types.Arg(DateTime, graphql_name='beforeTime', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('at_or_after_time', sgqlc.types.Arg(DateTime, graphql_name='atOrAfterTime', default=None)),
))
    )


class BallTelemetrySample(sgqlc.types.Type, Node):
    __schema__ = aaf_schema
    ball = sgqlc.types.Field(Ball, graphql_name='ball')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    orientation = sgqlc.types.Field(Quaternion, graphql_name='orientation')
    position_meters = sgqlc.types.Field(Point3D, graphql_name='positionMeters')
    position_yards = sgqlc.types.Field(Point3D, graphql_name='positionYards')
    time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='time')


class Coach(sgqlc.types.Type, Person, Node):
    __schema__ = aaf_schema
    avatar = sgqlc.types.Field('File', graphql_name='avatar')
    biography = sgqlc.types.Field(String, graphql_name='biography')
    birth_date = sgqlc.types.Field(Date, graphql_name='birthDate')
    career_summary = sgqlc.types.Field(String, graphql_name='careerSummary')
    common_name = sgqlc.types.Field(PersonName, graphql_name='commonName')
    height_millimeters = sgqlc.types.Field(Int, graphql_name='heightMillimeters')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    legal_name = sgqlc.types.Field(PersonName, graphql_name='legalName')
    name = sgqlc.types.Field(sgqlc.types.non_null(PersonName), graphql_name='name')
    personnel_notes = sgqlc.types.Field(String, graphql_name='personnelNotes')
    position = sgqlc.types.Field(CoachPosition, graphql_name='position')
    team = sgqlc.types.Field('Team', graphql_name='team')
    telemetry_samples_connection = sgqlc.types.Field(PersonPersonTelemetrySampleConnection, graphql_name='telemetrySamplesConnection', args=sgqlc.types.ArgDict((
        ('before_time', sgqlc.types.Arg(DateTime, graphql_name='beforeTime', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('at_or_after_time', sgqlc.types.Arg(DateTime, graphql_name='atOrAfterTime', default=None)),
))
    )
    title = sgqlc.types.Field(String, graphql_name='title')
    weight_grams = sgqlc.types.Field(Int, graphql_name='weightGrams')


class Division(sgqlc.types.Type, Node):
    __schema__ = aaf_schema
    abbreviation = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='abbreviation')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class Event(sgqlc.types.Type, Node):
    __schema__ = aaf_schema
    availability = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(EventAvailability)), graphql_name='availability')
    duration_seconds = sgqlc.types.Field(Int, graphql_name='durationSeconds')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    image = sgqlc.types.Field('File', graphql_name='image')
    short_description = sgqlc.types.Field(String, graphql_name='shortDescription')
    time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='time')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')


class File(sgqlc.types.Type, Node):
    __schema__ = aaf_schema
    content_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='contentType')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')


class Game(sgqlc.types.Type, Node):
    __schema__ = aaf_schema
    av_programs_connection = sgqlc.types.Field(GameAVProgramsConnection, graphql_name='avProgramsConnection', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    availability = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EventAvailability))), graphql_name='availability')
    away_team = sgqlc.types.Field('Team', graphql_name='awayTeam')
    away_team_edge = sgqlc.types.Field(GameTeamEdge, graphql_name='awayTeamEdge')
    balls_connection = sgqlc.types.Field(GameBallsConnection, graphql_name='ballsConnection', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    clock = sgqlc.types.Field(GameClock, graphql_name='clock')
    clock_history_connection = sgqlc.types.Field(GameClockHistoryConnection, graphql_name='clockHistoryConnection', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('before_time', sgqlc.types.Arg(DateTime, graphql_name='beforeTime', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('at_or_after_time', sgqlc.types.Arg(DateTime, graphql_name='atOrAfterTime', default=None)),
))
    )
    coin_tosses = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CoinToss)), graphql_name='coinTosses')
    default_avprogram = sgqlc.types.Field(AVProgram, graphql_name='defaultAVProgram')
    duration_milliseconds = sgqlc.types.Field(Int, graphql_name='durationMilliseconds')
    hls_master_playlist_url = sgqlc.types.Field(String, graphql_name='hlsMasterPlaylistURL')
    home_team = sgqlc.types.Field('Team', graphql_name='homeTeam')
    home_team_edge = sgqlc.types.Field(GameTeamEdge, graphql_name='homeTeamEdge')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    named_time_range = sgqlc.types.Field('NamedTimeRange', graphql_name='namedTimeRange')
    officials_connection = sgqlc.types.Field(GameOfficialsConnection, graphql_name='officialsConnection', args=sgqlc.types.ArgDict((
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    play_clock = sgqlc.types.Field(GamePlayClock, graphql_name='playClock')
    play_clock_history_connection = sgqlc.types.Field(GamePlayClockHistoryConnection, graphql_name='playClockHistoryConnection', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('at_or_after_time', sgqlc.types.Arg(DateTime, graphql_name='atOrAfterTime', default=None)),
        ('before_time', sgqlc.types.Arg(DateTime, graphql_name='beforeTime', default=None)),
))
    )
    players_connection = sgqlc.types.Field(GamePlayersConnection, graphql_name='playersConnection', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    plays_connection = sgqlc.types.Field(GamePlaysConnection, graphql_name='playsConnection', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('at_or_after_time', sgqlc.types.Arg(DateTime, graphql_name='atOrAfterTime', default=None)),
        ('before_time', sgqlc.types.Arg(DateTime, graphql_name='beforeTime', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
))
    )
    stadium = sgqlc.types.Field('Stadium', graphql_name='stadium')
    status = sgqlc.types.Field(GameStatus, graphql_name='status')
    status_history_connection = sgqlc.types.Field(GameStatusHistoryConnection, graphql_name='statusHistoryConnection', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before_time', sgqlc.types.Arg(DateTime, graphql_name='beforeTime', default=None)),
        ('at_or_after_time', sgqlc.types.Arg(DateTime, graphql_name='atOrAfterTime', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    subseason = sgqlc.types.Field(sgqlc.types.non_null(Subseason), graphql_name='subseason')
    telemetry_xdirection = sgqlc.types.Field(PrincipalWind, graphql_name='telemetryXDirection')
    ticketing_website_url = sgqlc.types.Field(String, graphql_name='ticketingWebsiteURL')
    time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='time')
    time_to_be_determined = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='timeToBeDetermined')
    timeouts_connection = sgqlc.types.Field(GameTimeoutsConnection, graphql_name='timeoutsConnection', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('at_or_after_time', sgqlc.types.Arg(DateTime, graphql_name='atOrAfterTime', default=None)),
        ('before_time', sgqlc.types.Arg(DateTime, graphql_name='beforeTime', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
))
    )


class NamedTimeRange(sgqlc.types.Type, Node):
    __schema__ = aaf_schema
    duration_milliseconds = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='durationMilliseconds')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    season = sgqlc.types.Field('Season', graphql_name='season')
    subseason = sgqlc.types.Field(sgqlc.types.non_null(Subseason), graphql_name='subseason')
    time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='time')


class Official(sgqlc.types.Type, Person, Node):
    __schema__ = aaf_schema
    avatar = sgqlc.types.Field(File, graphql_name='avatar')
    biography = sgqlc.types.Field(String, graphql_name='biography')
    birth_date = sgqlc.types.Field(Date, graphql_name='birthDate')
    common_name = sgqlc.types.Field(PersonName, graphql_name='commonName')
    creation_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='creationTime')
    height_millimeters = sgqlc.types.Field(Int, graphql_name='heightMillimeters')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    legal_name = sgqlc.types.Field(PersonName, graphql_name='legalName')
    name = sgqlc.types.Field(sgqlc.types.non_null(PersonName), graphql_name='name')
    personnel_notes = sgqlc.types.Field(String, graphql_name='personnelNotes')
    telemetry_samples_connection = sgqlc.types.Field(PersonPersonTelemetrySampleConnection, graphql_name='telemetrySamplesConnection', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('at_or_after_time', sgqlc.types.Arg(DateTime, graphql_name='atOrAfterTime', default=None)),
        ('before_time', sgqlc.types.Arg(DateTime, graphql_name='beforeTime', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    weight_grams = sgqlc.types.Field(Int, graphql_name='weightGrams')


class PersonTelemetrySample(sgqlc.types.Type, Node):
    __schema__ = aaf_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    orientation = sgqlc.types.Field(Quaternion, graphql_name='orientation')
    person = sgqlc.types.Field(Person, graphql_name='person')
    position_meters = sgqlc.types.Field(Point3D, graphql_name='positionMeters')
    position_yards = sgqlc.types.Field(Point3D, graphql_name='positionYards')
    time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='time')


class Play(sgqlc.types.Type, Node):
    __schema__ = aaf_schema
    creation_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='creationTime')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    direction = sgqlc.types.Field(PrincipalWind, graphql_name='direction')
    down = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='down')
    game_clock_seconds = sgqlc.types.Field(Int, graphql_name='gameClockSeconds')
    has_injury = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasInjury')
    has_penalty = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPenalty')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_complete = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isComplete')
    is_conversion = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isConversion')
    possession = sgqlc.types.Field(Possession, graphql_name='possession')
    quarter = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quarter')
    sequence = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='sequence')
    stats = sgqlc.types.Field(sgqlc.types.list_of(PlayStat), graphql_name='stats')
    time = sgqlc.types.Field(DateTime, graphql_name='time')
    type = sgqlc.types.Field(PlayType, graphql_name='type')
    yard_line = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yardLine')
    yard_line_team = sgqlc.types.Field(YardLineTeam, graphql_name='yardLineTeam')
    yards_to_go = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yardsToGo')


class Player(sgqlc.types.Type, Person, Node):
    __schema__ = aaf_schema
    agent = sgqlc.types.Field(Agent, graphql_name='agent')
    avatar = sgqlc.types.Field(File, graphql_name='avatar')
    biography = sgqlc.types.Field(String, graphql_name='biography')
    birth_date = sgqlc.types.Field(Date, graphql_name='birthDate')
    career_summary = sgqlc.types.Field(String, graphql_name='careerSummary')
    cfl_status = sgqlc.types.Field(PlayerLeagueStatus, graphql_name='cflStatus')
    common_name = sgqlc.types.Field(PersonName, graphql_name='commonName')
    community_activities_summary = sgqlc.types.Field(String, graphql_name='communityActivitiesSummary')
    creation_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='creationTime')
    email_address = sgqlc.types.Field(String, graphql_name='emailAddress')
    games_connection = sgqlc.types.Field(PlayerGamesConnection, graphql_name='gamesConnection', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
))
    )
    height_millimeters = sgqlc.types.Field(Int, graphql_name='heightMillimeters')
    hometown = sgqlc.types.Field(Address, graphql_name='hometown')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_allocated = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAllocated')
    jersey_number = sgqlc.types.Field(Int, graphql_name='jerseyNumber')
    legal_name = sgqlc.types.Field(PersonName, graphql_name='legalName')
    name = sgqlc.types.Field(sgqlc.types.non_null(PersonName), graphql_name='name')
    ncaa_fbcareer = sgqlc.types.Field(PlayerNCAAFBCareer, graphql_name='ncaaFBCareer')
    nfl_status = sgqlc.types.Field(PlayerLeagueStatus, graphql_name='nflStatus')
    personnel_notes = sgqlc.types.Field(String, graphql_name='personnelNotes')
    phone_number = sgqlc.types.Field(String, graphql_name='phoneNumber')
    platoon = sgqlc.types.Field(Platoon, graphql_name='platoon')
    position = sgqlc.types.Field(PlayerPosition, graphql_name='position')
    roster_status = sgqlc.types.Field(PlayerRosterStatus, graphql_name='rosterStatus')
    schools_connection = sgqlc.types.Field(PlayerSchoolsConnection, graphql_name='schoolsConnection', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    seasons_connection = sgqlc.types.Field(PlayerSeasonsConnection, graphql_name='seasonsConnection', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
))
    )
    sportradar_ncaafbid = sgqlc.types.Field(String, graphql_name='sportradarNCAAFBId')
    team = sgqlc.types.Field('Team', graphql_name='team')
    telemetry_samples_connection = sgqlc.types.Field(PersonPersonTelemetrySampleConnection, graphql_name='telemetrySamplesConnection', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('at_or_after_time', sgqlc.types.Arg(DateTime, graphql_name='atOrAfterTime', default=None)),
        ('before_time', sgqlc.types.Arg(DateTime, graphql_name='beforeTime', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    transactions_connection = sgqlc.types.Field(PlayerPlayerTransactionsConnection, graphql_name='transactionsConnection', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('at_or_after_date', sgqlc.types.Arg(Date, graphql_name='atOrAfterDate', default=None)),
        ('before_date', sgqlc.types.Arg(Date, graphql_name='beforeDate', default=None)),
))
    )
    weight_grams = sgqlc.types.Field(Int, graphql_name='weightGrams')


class PlayerTransaction(sgqlc.types.Type, Node):
    __schema__ = aaf_schema
    date = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='date')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    player = sgqlc.types.Field(sgqlc.types.non_null(Player), graphql_name='player')
    roster_status = sgqlc.types.Field(PlayerRosterStatus, graphql_name='rosterStatus')
    team = sgqlc.types.Field('Team', graphql_name='team')
    waiver_deadline = sgqlc.types.Field(DateTime, graphql_name='waiverDeadline')


class School(sgqlc.types.Type, Node):
    __schema__ = aaf_schema
    abbreviation = sgqlc.types.Field(String, graphql_name='abbreviation')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class Season(sgqlc.types.Type, Node):
    __schema__ = aaf_schema
    aggregated_team_stats = sgqlc.types.Field(AggregatedTeamStats, graphql_name='aggregatedTeamStats', args=sgqlc.types.ArgDict((
        ('aggregator', sgqlc.types.Arg(sgqlc.types.non_null(SeasonAggregatedTeamStatsAggregator), graphql_name='aggregator', default=None)),
        ('opposition', sgqlc.types.Arg(Boolean, graphql_name='opposition', default=None)),
))
    )
    games_connection = sgqlc.types.Field(SeasonGamesConnection, graphql_name='gamesConnection', args=sgqlc.types.ArgDict((
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    named_time_ranges_connection = sgqlc.types.Field(SeasonNamedTimeRangesConnection, graphql_name='namedTimeRangesConnection', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    year = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='year')


class Stadium(sgqlc.types.Type, Node):
    __schema__ = aaf_schema
    address = sgqlc.types.Field(Address, graphql_name='address')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class Team(sgqlc.types.Type, Node):
    __schema__ = aaf_schema
    abbreviation = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='abbreviation')
    avatar = sgqlc.types.Field(File, graphql_name='avatar')
    background = sgqlc.types.Field(File, graphql_name='background', args=sgqlc.types.ArgDict((
        ('style', sgqlc.types.Arg(sgqlc.types.non_null(TeamBackgroundStyle), graphql_name='style', default=None)),
))
    )
    coach = sgqlc.types.Field(Coach, graphql_name='coach', args=sgqlc.types.ArgDict((
        ('position', sgqlc.types.Arg(CoachPosition, graphql_name='position', default=None)),
))
    )
    coaches_connection = sgqlc.types.Field(TeamCoachesConnection, graphql_name='coachesConnection', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    colors = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Color)), graphql_name='colors')
    division = sgqlc.types.Field(Division, graphql_name='division')
    facebook_handle = sgqlc.types.Field(String, graphql_name='facebookHandle')
    games_connection = sgqlc.types.Field(TeamGamesConnection, graphql_name='gamesConnection', args=sgqlc.types.ArgDict((
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('at_or_after_time', sgqlc.types.Arg(DateTime, graphql_name='atOrAfterTime', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('before_time', sgqlc.types.Arg(DateTime, graphql_name='beforeTime', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    instagram_handle = sgqlc.types.Field(String, graphql_name='instagramHandle')
    logo = sgqlc.types.Field(File, graphql_name='logo', args=sgqlc.types.ArgDict((
        ('style', sgqlc.types.Arg(TeamLogoStyle, graphql_name='style', default=None)),
))
    )
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    nickname = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nickname')
    players_connection = sgqlc.types.Field(TeamPlayersConnection, graphql_name='playersConnection', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('platoon', sgqlc.types.Arg(Platoon, graphql_name='platoon', default=None)),
        ('position', sgqlc.types.Arg(PlayerPosition, graphql_name='position', default=None)),
        ('roster_status', sgqlc.types.Arg(PlayerRosterStatus, graphql_name='rosterStatus', default=None)),
))
    )
    region_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='regionName')
    seasons_connection = sgqlc.types.Field(TeamSeasonsConnection, graphql_name='seasonsConnection', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
))
    )
    shop_website_url = sgqlc.types.Field(String, graphql_name='shopWebsiteURL')
    stadium = sgqlc.types.Field(sgqlc.types.non_null(Stadium), graphql_name='stadium')
    ticketing_website_url = sgqlc.types.Field(String, graphql_name='ticketingWebsiteURL')
    twitter_handle = sgqlc.types.Field(String, graphql_name='twitterHandle')
    website_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='websiteURL')
    wordmark = sgqlc.types.Field(File, graphql_name='wordmark', args=sgqlc.types.ArgDict((
        ('style', sgqlc.types.Arg(TeamWordmarkStyle, graphql_name='style', default=None)),
))
    )


class Timeout(sgqlc.types.Type, Node):
    __schema__ = aaf_schema
    creation_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='creationTime')
    game_clock_seconds = sgqlc.types.Field(Int, graphql_name='gameClockSeconds')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    sequence = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='sequence')
    time = sgqlc.types.Field(DateTime, graphql_name='time')
    type = sgqlc.types.Field(TimeoutType, graphql_name='type')


class U2FDevice(sgqlc.types.Type, Node):
    __schema__ = aaf_schema
    cloning_detected = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='cloningDetected')
    creation_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='creationTime')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    key_handle_base64 = sgqlc.types.Field(String, graphql_name='keyHandleBase64')


class User(sgqlc.types.Type, Node):
    __schema__ = aaf_schema
    avatar = sgqlc.types.Field(File, graphql_name='avatar')
    creation_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='creationTime')
    email_address = sgqlc.types.Field(String, graphql_name='emailAddress')
    front_end_preferences = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FrontEndPreference))), graphql_name='frontEndPreferences', args=sgqlc.types.ArgDict((
        ('namespace', sgqlc.types.Arg(String, graphql_name='namespace', default=None)),
))
    )
    handle = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='handle')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    level = sgqlc.types.Field(sgqlc.types.non_null('UserLevel'), graphql_name='level')
    next_level = sgqlc.types.Field('UserLevel', graphql_name='nextLevel')
    phone_number = sgqlc.types.Field(String, graphql_name='phoneNumber')
    roles = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(UserRole)), graphql_name='roles')
    u2f_devices = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(U2FDevice)), graphql_name='u2fDevices')
    xp = sgqlc.types.Field(sgqlc.types.non_null(LongInt), graphql_name='xp')


class UserLevel(sgqlc.types.Type, Node):
    __schema__ = aaf_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')
    required_xp = sgqlc.types.Field(sgqlc.types.non_null(LongInt), graphql_name='requiredXP')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')



########################################################################
# Unions
########################################################################
