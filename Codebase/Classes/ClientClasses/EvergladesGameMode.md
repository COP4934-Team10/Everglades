# EvergladesGameMode


**Class Type**&nbsp; &nbsp; &nbsp; &nbsp; Blueprint  
**Parent Class** &nbsp; &nbsp; GameModeBase  

## Variables
|Variable                   |Type                               |Description    |
|---------------------------|-----------------------------------|---------------|
|**ActiveGroups**           |*Array\<SwarmGroup*\>              ||
|**AITimer**                |*Timer Handle*                     ||
|**CamTargetGroup**         |*SwarmGroup*                       ||
|**CurrentFocusGroup**      |*SwarmGroup*                       ||
|**CurrentFocusGroupID**    |*Integer*                          ||
|**CurrentTurn**            |*Integer*                          ||
|**DefaultSceneRoot**       |*SceneComponent*                   ||
|**DefaultViewTarget**      |*Actor*                            ||
|**Events**                 |*Evg Events*                       ||
|**EventsCompleted**        |*Integer*                          ||
|**EventsSent**             |*Integer*                          ||
|**FolderName**             |*String*                           ||
|**GameResultString**       |*String*                           ||
|**GameStateRef**           |*EvergladesGameState*              ||
|**HUDRandomRef**           |*SpectatorHUD_Random*              ||
|**HUDRef**                 |*SpectatorHUD*                     ||
|**ImagesRemaining**        |*Integer*                          ||
|**ImageURLs**              |*Array\<String\>*                  ||
|**LoadingIndex**           |*Integer*                          ||
|**MainMenuRef**            |*MainMenu*                         ||
|**MapNodes**               |*Integer*                          ||
|**MapVisible**             |*Boolean*                          ||
|**MatchStarted**           |*Boolean*                          ||
|**NodeCombat**             |*Array\<NodeCombatState\>*         ||
|**NodeControl**            |*Array\<Float\>*                   ||
|**NodePoints**             |*Array\<NodePoint\>*               ||
|**NumUnits**               |*Array\<Integer\>*                 ||
|**P0_TurnImages**          |*Map\<Integer, Texture2DDynamic\>* ||
|**P1Score**                |*Integer*                          ||
|**P1_TurnImages**          |*Map\<Integer, Texture2DDynamic\>* ||
|**P2Score**                |*Integer*                          ||
|**SimplifiedMap**          |*Boolean*                          ||
|**SimplifiedMapSequence**  |*LevelSequenceActor*               ||
|**SpectatorPawn**          |*EvergladesSpectatorPawn*          ||
|**TurnComplete**           |*Boolean*                          ||
|**TurnImages**             |*Array\<Texture2DDynamic\>*        ||
|**Units**                  |*Array\<SwarmUnit\>*               ||
|**UseCamAI**               |*Boolean*                          ||
|**UsingFollow**            |*Boolean*                          ||

## Functions
[**CalculateNodeControl**](../../Methods/ClientMethods/CalculateNodeControl.md)  
[**ConstructionScript**](../../Methods/ClientMethods/ConstructionScript_EvergladesGameMode.md)  
[**CreateGroup**](../../Methods/ClientMethods/CreateGroup.md)  
[**GetAvailableMoveNode**](../../Methods/ClientMethods/GetAvailableMoveNode.md)  
[**GetConnectionSpline**](../../Methods/ClientMethods/GetConnectionSpline.md)  
[**GetGroup**](../../Methods/ClientMethods/GetGroup.md)  
[**GetNode**](../../Methods/ClientMethods/GetNode.md)  
[**GetNumPlayerUnits**](../../Methods/ClientMethods/GetNumPlayerUnits.md)  
[**GetTeamMV**](../../Methods/ClientMethods/GetTeamMV.md)  
[**GetUnit**](../../Methods/ClientMethods/GetUnit.md)  
[**LogMapData**](../../Methods/ClientMethods/LogMapData.md)  
[**RemoveGroup**](../../Methods/ClientMethods/RemoveGroup.md)  
[**RemovePlayerUnit**](../../Methods/ClientMethods/RemovePlayerUnit.md)  

## Events
[**AddHUD**](../../Events/AddHUD.md)  
[**AddUnit**](../../Events/AddUnit.md)  
[**ArrivedEvent**](../../Events/ArrivedEvent_EvergladesGameMode.md)  
[**DebugWinner**](../../Events/DebugWinner.md)  
[**EndMatch**](../../Events/EndMatch.md)  
[**Event BeginPlay**](../../Events/BeginPlay_EvergladesGameMode.md)  
[**Event Tick**](../../Events/Tick_EvergladesGameMode.md)  
[**InTransitEvent**](../../Events/InTransitEvent.md)  
[**LoadEvents**](../../Events/LoadEvents.md)  
[**LoadImages**](../../Events/LoadImages.md)  
[**OnEventCompleted**](../../Events/OnEventCompleted.md)  
[**ProcessCombatEvent**](../../Events/ProcessCombatEvent.md)  
[**ProcessNodeControlUpdate**](../../Events/ProcessNodeControlUpdate.md)  
[**ProcessTransferUnitsUpdate**](../../Events/ProcessTransferUnitsUpdate.md)  
[**RdyToMoveEvent**](../../Events/RdyToMoveEvent.md)  
[**RunEvents**](../../Events/RunEvents.md)  
[**SetArenaCamTarget**](../../Events/SetArenaCamTarget.md)  
[**SetFocusGroup**](../../Events/SetFocusGroup.md)  
[**SetFollowCam**](../../Events/SetFollowCam.md)  
[**SetFreeCam**](../../Events/SetFreeCam.md)  
[**StartCamAI**](../../Events/StartCamAI.md)  
[**StopCamAI**](../../Events/StopCamAI.md)  
[**TickCam**](../../Events/TickCam.md)  
[**ToggleCamAI**](../../Events/ToggleCamAI.md)  
[**ToggleMap**](../../Events/ToggleMap.md)  
[**ToggleSimplifiedMap**](../../Events/ToggleSimplifiedMap_EvergladesGameMode.md)  
[**TurnPauseToggle**](../../Events/TurnPauseToggle.md)  
[**TurnTimeout**](../../Events/TurnTimeout.md)  
[**UpdateCamAI**](../../Events/UpdateCamAI.md)  

## Event Dispatchers
[**ChangeCamMode**](../../Dispatchers/ChangeCamMode.md)  
[**ImageLoadComplete**](../../Dispatchers/ImageLoadComplete.md)  

## Macros
[**GetGroup_Macro**](../../Macros/GetGroup_Macro.md)  
[**GetLastIndex**](../../Macros/GetLastIndex.md)  
[**IDExists**](../../Macros/IDExists.md)  
[**ImageURLProcessing**](../../Macros/ImageURLProcessing.md)  
[**Message_CombatEvent**](../../Macros/Message_CombatEvent.md)  
[**Message_CombatUpdate**](../../Macros/Message_CombatUpdate.md)  
[**Message_ControlUpdate**](../../Macros/Message_ControlUpdate.md)  
[**Message_CreateNewGroup**](../../Macros/Message_CreateNewGroup.md)  
[**Message_Disband**](../../Macros/Message_Disband.md)  
[**Message_Init**](../../Macros/Message_Init.md)  
[**Message_Move**](../../Macros/Message_Move.md)  
[**Message_Scores**](../../Macros/Message_Scores.md)  
[**Message_TransferUnits**](../../Macros/Message_TransferUnits.md)  
[**ParsePosition**](../../Macros/ParsePosition.md)  
[**ParseScoreString**](../../Macros/ParseScoreString.md)  