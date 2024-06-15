from __future__ import annotations

from abc import ABCMeta
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, overload

from attrs import define

from .response import CommandResponse

if TYPE_CHECKING:
    from .server import Server

from .utils import WorldCoordinate, WorldCoordinates, rawtext


@define
class Context(metaclass=ABCMeta):
    """Context passed to event handlers."""

    _server: Server

    @property
    def server(self) -> Server:
        """A reference to the server object this context belongs to."""
        return self._server


@define
class GameContext(Context, metaclass=ABCMeta):
    """Context passed to game event handlers."""

    _server: Server
    _data: Mapping[str, Any]

    @property
    def data(self) -> Mapping[str, Any]:
        """A reference to the raw data of the event received."""
        return self._data


@define
class BlockBrokenContext(GameContext):
    @property
    def id(self) -> str:
        return self._data["block"]["id"]

    @property
    def namespace(self) -> str:
        return self._data["block"]["namespace"]

    @property
    def count(self) -> int:
        return self._data["count"]

    @property
    def destruction_method(self) -> int:
        return self._data["destructionMethod"]

    @property
    def player(self) -> str:
        return self._data["player"]

    @property
    def tool(self) -> str | None:
        try:
            return self._data["tool"]["id"]
        except KeyError:
            return None


@define
class BlockPlacedContext(GameContext):
    @property
    def id(self) -> str:
        return self._data["block"]["id"]

    @property
    def namespace(self) -> str:
        return self._data["block"]["namespace"]

    @property
    def count(self) -> int:
        return self._data["count"]

    @property
    def player(self) -> str:
        return self._data["player"]

    @property
    def player_position(self) -> WorldCoordinates:
        xyz = self._data["player"]["position"]
        return WorldCoordinates(
            (
                WorldCoordinate(xyz["x"]),
                WorldCoordinate(xyz["y"]),
                WorldCoordinate(xyz["z"]),
            )
        )

    @property
    def tool(self) -> str | None:
        try:
            return self._data["tool"]["id"]
        except KeyError:
            return None


@define
class EndOfDayContext(GameContext):
    @property
    def player_position(self) -> WorldCoordinates:
        xyz = self._data["player"]["position"]
        return WorldCoordinates(
            (
                WorldCoordinate(xyz["x"]),
                WorldCoordinate(xyz["y"]),
                WorldCoordinate(xyz["z"]),
            )
        )


@define
class PlayerMessageContext(GameContext):
    @property
    def message(self) -> str:
        """The message."""
        return self._data["message"]

    @property
    def receiver(self) -> str | None:
        """The receiver of the message.

        .. note:: This may be ``None`` if there was no specific receiver.
        """
        return self._data.get("receiver")

    @property
    def sender(self) -> str:
        """The sender of the message."""
        return self._data["sender"]

    @property
    def type(self) -> str:
        """The type of the message."""
        return self._data["type"]

    @overload
    async def reply(
        self, message: str, *, raw: bool = False, wait: Literal[False]
    ) -> None:
        ...

    @overload
    async def reply(
        self, message: str, *, raw: bool = False, wait: Literal[True] = True
    ) -> CommandResponse:
        ...

    async def reply(
        self, message: str, *, raw: bool = False, wait: bool = True
    ) -> CommandResponse | None:
        if raw:
            command = f"tellraw {self.sender} {rawtext(message)}"
        else:
            command = f"tell {self.sender} {message}"
        return await self.server.run(command, wait=wait)  # type: ignore


@define
class PlayerTransformContext(GameContext):
    @property
    def player(self) -> str:
        return self._data["player"]["name"]

    @property
    def player_position(self) -> WorldCoordinates:
        xyz = self._data["player"]["position"]
        return WorldCoordinates(
            (
                WorldCoordinate(xyz["x"]),
                WorldCoordinate(xyz["y"]),
                WorldCoordinate(xyz["z"]),
            )
        )


@define
class PlayerTravelledContext(GameContext):
    @property
    def underwater(self) -> bool:
        return self._data["isUnderwater"]

    @property
    def meters(self) -> float:
        return self._data["metersTravelled"]

    @property
    def player(self) -> str:
        return self._data["player"]["name"]

    @property
    def player_position(self) -> WorldCoordinates:
        xyz = self._data["player"]["position"]
        return WorldCoordinates(
            (
                WorldCoordinate(xyz["x"]),
                WorldCoordinate(xyz["y"]),
                WorldCoordinate(xyz["z"]),
            )
        )

    @property
    def travel_method(self) -> int:
        return self._data["travelMethod"]


@define(init=False)
class ServerContext(Context, metaclass=ABCMeta):
    """Context passed to server event handlers."""


def get_game_context(name: str) -> type[GameContext]:
    return {
        # TODO: implementation of the commented events
        # "additional_content_loaded": AdditionalContentLoadedContext,
        # "agent_command": AgentCommandContext,
        # "api_init": ApiInitContext,
        # "app_paused": AppPausedContext,
        # "app_resumed": AppResumedContext,
        # "app_suspended": AppSuspendedContext,
        # "award_achievement": AwardAchievementContext,
        "block_broken": BlockBrokenContext,
        "block_placed": BlockPlacedContext,
        # "board_text_updated": BoardTextUpdatedContext,
        # "boss_killed": BossKilledContext,
        # "camera_used": CameraUsedContext,
        # "cauldron_used": CauldronUsedContext,
        # "configuration_changed": ConfigurationChangedContext,
        # "connection_failed": ConnectionFailedEvent,
        # "crafting_session_completed": CraftingSessionCompletedContext,
        "end_of_day": EndOfDayContext,
        # "entity_spawned": EntitySpawnedContext,
        # "file_transmission_cancelled": FileTransmissionCancelledContext,
        # "file_transmission_completed": FileTransmissionCompletedContext,
        # "file_transmission_started": FileTransmissionStartedContext,
        # "first_time_client_open": FirstTimeClientOpenContext,
        # "focus_gained": FocusGainedContext,
        # "focus_lost": FocusLostContext,
        # "game_session_complete": GameSessionCompleteContext,
        # "game_session_start": GameSessionStartContext,
        # "hardware_info": HardwareInfoContext,
        # "has_new_content": HasNewContentContext,
        # "item_acquired": ItemAcquiredContext,
        # "item_crafted": ItemCraftedContext,
        # "item_destroyed": ItemDestroyedContext,
        # "item_dropped": ItemDroppedContext,
        # "item_enchanted": ItemEnchantedContext,
        # "item_smelted": ItemSmeltedContext,
        # "item_used": ItemUsedContext,
        # "join_canceled": JoinCanceledContext,
        # "jukebox_used": JukeboxUsedContext,
        # "license_census": LicenseCensusContext,
        # "mascot_created": MascotCreatedContext,
        # "menu_shown": MenuShownContext,
        # "mob_interacted": MobInteractedContext,
        # "mob_killed": MobKilledContext,
        # "multiplayer_connection_state_changed": MultiplayerConnectionStateChangedContext,
        # "multiplayer_round_end": MultiplayerRoundEndContext,
        # "multiplayer_round_start": MultiplayerRoundStartContext,
        # "npc_properties_updated": NpcPropertiesUpdatedContext,
        # "options_updated": OptionsUpdatedContext,
        # "performance_metrics": PerformanceMetricsContext,
        # "player_bounced": PlayerBouncedContext,
        # "player_died": PlayerDiedContext,
        # "player_join": PlayerJoinContext,
        # "player_leave": PlayerLeaveContext,
        "player_message": PlayerMessageContext,
        # "player_teleported": PlayerTeleportedContext,
        "player_transform": PlayerTransformContext,
        "player_travelled": PlayerTravelledContext,
        # "portal_built": PortalBuiltContext,
        # "portal_used": PortalUsedContext,
        # "portfolio_exported": PortfolioExportedContext,
        # "potion_brewed": PotionBrewedContext,
        # "purchase_attempt": PurchaseAttemptContext,
        # "purchase_resolved": PurchaseResolvedContext,
        # "regional_popup": RegionalPopupContext,
        # "responded_to_accept_content": RespondedToAcceptContentContext,
        # "screen_changed": ScreenChangedContext,
        # "screen_heartbeat": ScreenHeartbeatContext,
        # "sign_in_to_edu": SignInToEduContext,
        # "sign_in_to_xbox_live": SignInToXboxLiveContext,
        # "sign_out_of_xbox_live": SignOutOfXboxLiveContext,
        # "special_mob_built": SpecialMobBuiltContext,
        # "start_client": StartClientContext,
        # "start_world": StartWorldContext,
        # "text_to_speech_toggled": TextToSpeechToggledContext,
        # "ugc_download_completed": UgcDownloadCompletedContext,
        # "ugc_download_started": UgcDownloadStartedContext,
        # "upload_skin": UploadSkinContext,
        # "vehicle_exited": VehicleExitedContext,
        # "world_exported": WorldExportedContext,
        # "world_files_listed": WorldFilesListedContext,
        # "world_generated": WorldGeneratedContext,
        # "world_loaded": WorldLoadedContext,
        # "world_unloaded": WorldUnloadedContext,
    }[name]


@define
class ReadyContext(ServerContext):
    _server: Server
    _host: str
    _port: int

    @property
    def host(self) -> str:
        return self._host

    @property
    def port(self) -> int:
        return self._port


@define
class ConnectContext(ServerContext):
    _server: Server


@define
class DisconnectContext(ServerContext):
    _server: Server
