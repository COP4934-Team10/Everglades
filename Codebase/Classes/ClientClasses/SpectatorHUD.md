# SpectatorHUD


**Class Type**&nbsp; &nbsp; &nbsp; &nbsp; Blueprint  
**Parent Class** &nbsp; &nbsp; User Widget  

## Variables
|Variable                   |Type                       |Description    |
|---------------------------|---------------------------|---------------|
|**Arena_Scrollbox**        |*ScrollBox*                ||
|**Arenas_Btn**             |*Button*                   ||
|**BlueBase**               |*Image*                    ||
|**BlueTeam_MV**            |*Image*                    ||
|**BottomBar**              |*Image*                    ||
|**BottomTextHolder**       |*Image*                    ||
|**Btn_Maximize**           |*Button*                   || 
|**Btn_Pause**              |*Button*                   ||
|**CameraSidebar_Slide**    |*WidgetAnimation*          ||
|**ExitButton**             |*Button*                   ||
|**GameModeRef**            |*EverGladesGameMode*       ||
|**Group_ScrollBox**        |*ScrollBox*                ||
|**Groups_Btn**             |*Button*                   ||
|**HUD_LargeMap**           |*HUD_LargeMap*             ||
|**HUD_MiniMap_Zone_A**     |*HUD_MiniMap_Zone*         ||
|**HUD_MiniMap_Zone_B**     |*HUD_MiniMap_Zone*         ||
|**HUD_MiniMap_Zone_Base_1**|*HUD_MiniMap_Zone*         ||
|**HUD_MiniMap_Zone_Base_2**|*HUD_MiniMap_Zone*         ||
|**HUD_MiniMap_Zone_C**     |*HUD_MiniMap_Zone*         ||
|**HUD_MiniMap_Zone_D**     |*HUD_MiniMap_Zone*         ||
|**HUD_MiniMap_Zone_E**     |*HUD_MiniMap_Zone*         ||
|**HUD_MiniMap_Zone_F**     |*HUD_MiniMap_Zone*         ||
|**HUD_MiniMap_Zone_G**     |*HUD_MiniMap_Zone*         ||
|**HUD_MiniMap_Zone_H**     |*HUD_MiniMap_Zone*         ||
|**HUD_MiniMap_Zone_I**     |*HUD_MiniMap_Zone*         ||
|**HUD_UnitLoss_Blue**      |*HUD_UnitLoss*             ||
|**HUD_UnitLoss_Red**       |*HUD_UnitLoss*             ||
|**HUD_Winner**             |*HUD_Winner*               ||
|**LargeMap**               |*WidgetAnimation*          ||
|**LargeMap_Visible**       |*Boolean*                  ||
|**MachineVisionPanel**     |*CanvasPanel*              ||
|**Map**                    |*Image*                    ||
|**MapWorldAnchor_BR**      |*Vector*                   ||
|**MapworldAnchor_TL**      |*Vector*                   ||
|**MiniMap_Base**           |*Image*                    ||
|**MV_Toggle**              |*Button*                   ||
|**PauseButtonStyle**       |*ButtonStyle Struct*       ||
|**PlayButtonStyle**        |*ButtonStyle Struct*       ||
|**Player1_ZoneControl**    |*ProgressBar*              ||
|**Player2_ZoneControl**    |*ProgressBar*              ||
|**PlayerPawn**             |*EvergladesSpectatorPawn*  ||
|**RedBase**                |*Image*                    ||
|**RedTeam_MV**             |*Image*                    ||
|**ReturnMenu**             |*Button*                   ||
|**ScoreAndUnitsHousing**   |*Image*                    ||
|**SidebarState**           |*Integer*                  ||
|**SideDetail**             |*Image*                    ||
|**Side_Detail_L**          |*Image*                    ||
|**StateText**              |*Text*                     ||
|**Team1_LastUnits**        |*Integer*                  ||
|**Team2_LastUnits**        |*Integer*                  ||
|**Team1UnitText**          |*Text*                     ||
|**Team2UnitText**          |*Text*                     ||
|**Time_Housing**           |*Image*                    ||
|**Timeline**               |*ProgressBar*              ||
|**TopBar**                 |*Image*                    ||
|**ZoneControl_Fill**       |*Image*                    ||
|**ZoneControl_Housing**    |*Image*                    ||
|**ZoneControl_Tine**       |*Image*                    ||

## Functions
[**GetBlueTeamMV_Turn**](../../Methods/ClientMethods/GetBlueTeamMV_Turn.md)  
[**GetCameraText**](../../Methods/ClientMethods/GetCameraText.md)  
[**GetPlayer1Score**](../../Methods/ClientMethods/GetPlayer1Score.md)  
[**GetPlayer2Score**](../../Methods/ClientMethods/GetPlayer2Score.md)  
[**GetPlayer1ZoneControlPercent**](../../Methods/ClientMethods/GetPlayer1ZoneControlPercent.md)  
[**GetPlayer2ZoneControlPercent**](../../Methods/ClientMethods/GetPlayer2ZoneControlPercent.md)  
[**GetRedTeamMV_Turn**](../../Methods/ClientMethods/GetRedTeamMV_Turn.md)  
[**GetTeam1UnitText**](../../Methods/ClientMethods/GetTeam1UnitText.md)  
[**GetTeam2UnitText**](../../Methods/ClientMethods/GetTeam2UnitText.md)  
[**GetTimelinePercent**](../../Methods/ClientMethods/GetTimelinePercent.md)  
[**GetTurnText**](../../Methods/ClientMethods/GetTurnText.md)  
[**GetWinText**](../../Methods/ClientMethods/GetWinText.md)  

## Events
[**Event Construct**](../../Events/Construct_SpectatorHUD.md)  
[**Event Tick**](../../Events/Tick_SpectatorHUD.md)  
[**GetPlayerPawn**](../../Events/GetPlayerPawn.md)  
[**HideMap**](../../Events/HideMap.md)  
[**Map_SetNodes**](../../Events/Map_SetNodes.md)  
[**On Clicked(Arenas_Btn)**](../../Events/Clicked_Arenas_Btn.md)  
[**On Clicked(Btn_Maximize)**](../../Events/Clicked_Btn_Maximize.md)  
[**On Clicked(Btn_Pause)**](../../Events/Clicked_Btn_Pause.md)  
[**On Clicked(ExitButton)**](../../Events/Clicked_ExitButton_SpectatorHUD.md)  
[**On Clicked(Groups_Btn)**](../../Events/Clicked_Groups_Btn.md)  
[**On Clicked(MV_Toggle)**](../../Events/Clicked_MV_Toggle.md)  
[**On Clicked(ReturnMenu)**](../../Events/Clicked_ReturnMenu.md)  
[**RemoveGroupIndicator**](../../Events/RemoveGroupIndicator.md)  
[**ToggleSimplifiedMap**](../../Events/ToggleSimplifiedMap_SpectatorHUD.md)  
[**Winner**](../../Events/Winner.md)  

## Event Dispatchers
**None**

## Macros
[**GetZoneControlAngle**](../../Macros/GetZoneControlAngle.md)  
[**WorldPosToMapPos**](../../Macros/WorldPosToMapPos.md)  