MAX_COMMAND_PROCESSING = 100
"""The amount of commands the client can process at a time without responding.

This is already handleded internally so there is usually no need to use
this. You can think of the client managing a FIFO queue of command requests
with a capacity of 100. The client pops out the first entered command request
and sends a command response bback to the server. When the server tries to
send a command request while the queue is already full, then the command will
never be executed and an error will be sent by the client.

.. mermaid::
    :caption: An example of an interaction between the server and a client.
    
    %%{init: {'theme': 'dark'}}%%
    sequenceDiagram
        Server-)Client: Command Request
        Server-)Client: Command Request
        Server-)Client: Command Request
        Client-)Server: Command Response
        loop 98 times
            Server-)Client: Command Request
        end
        Server-xClient: Command Request
        loop 98 times
        	Client-)Server: Command Response
        end
"""

NAME = "External"
"""The name of the server displayed in the game.

This name is displayed left to the message when the ``say`` command is used. Therefore
it is usually preferred to use ``tellraw`` instead.
"""

MINECRAFT_VERSION = "1.19.70"
"""The Minecraft version to use for the command syntax. This usually has no big impact."""

GAME_EVENTS = [
    "additional_content_loaded",
    "agent_command",
    "agent_created",
    "api_init",
    "app_paused",
    "app_resumed",
    "app_suspended",
    "award_achievement",
    "block_broken",
    "block_placed",
    "board_text_updated",
    "boss_killed",
    "camera_used",
    "cauldron_used",
    "configuration_changed",
    "connection_failed",
    "crafting_session_completed",
    "end_of_day",
    "entity_spawned",
    "file_transmission_cancelled",
    "file_transmission_completed",
    "file_transmission_started",
    "first_time_client_open",
    "focus_gained",
    "focus_lost",
    "game_session_complete",
    "game_session_start",
    "hardware_info",
    "has_new_content",
    "item_acquired",
    "item_crafted",
    "item_destroyed",
    "item_dropped",
    "item_enchanted",
    "item_smelted",
    "item_used",
    "join_canceled",
    "jukebox_used",
    "license_census",
    "mascot_created",
    "menu_shown",
    "mob_interacted",
    "mob_killed",
    "multiplayer_connection_state_changed",
    "multiplayer_round_end",
    "multiplayer_round_start",
    "npc_properties_updated",
    "options_updated",
    "performance_metrics",
    "player_bounced",
    "player_died",
    "player_join",
    "player_leave",
    "player_message",
    "player_teleported",
    "player_transform",
    "player_travelled",
    "portal_built",
    "portal_used",
    "portfolio_exported",
    "potion_brewed",
    "purchase_attempt",
    "purchase_resolved",
    "regional_popup",
    "responded_to_accept_content",
    "screen_changed",
    "screen_heartbeat",
    "sign_in_to_edu",
    "sign_in_to_xbox_live",
    "sign_out_of_xbox_live",
    "special_mob_built",
    "start_client",
    "start_world",
    "text_to_speech_toggled",
    "ugc_download_completed",
    "ugc_download_started",
    "upload_skin",
    "vehicle_exited",
    "world_exported",
    "world_files_listed",
    "world_generated",
    "world_loaded",
    "world_unloaded",
]
"""A list of game events the server can subcribe to.

.. note:: Some of these events may not work or are useless in a way.
"""
