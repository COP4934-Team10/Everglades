# SwarmGroup


**Class Type**&nbsp; &nbsp; &nbsp; &nbsp; Blueprint  
**Parent Class** &nbsp; &nbsp; Actor  

## Variables
|Variable                       |Type                       |Description    |
|-------------------------------|---------------------------|---------------|
|**Cube**                       |*StaticMeshComponent*      ||
|**CurrentConnectionSpline**    |*ConnectionSpline*         ||
|**CurrentDistanceAlongSpline** |*Float*                    ||
|**CurrentNode**                |*Integer*                  ||
|**CurrentTargetLocation**      |*Vector*                   ||
|**DefaultSceneRoot**           |*SceneComponent*           ||
|**FacingDirection**            |*Rotator*                  ||
|**GameModeRef**                |*EvergladesGameMode*       ||
|**GroupHP**                    |*Float*                    ||
|**GroupID**                    |*Integer*                  ||
|**GroupSpeed**                 |*Float*                    ||
|**GroupTargetLocation**        |*Vector*                   ||
|**GroupUnits**                 |*Array\<SwarmUnit\>*       ||
|**InNode**                     |*NodePoint*                ||
|**MovementDir**                |*Vector*                   ||
|**PlayerID**                   |*Integer*                  ||
|**PotentialAttackers**         |*Array\<SwarmGroup\>*      ||
|**ReceivedMoveOrder**          |*Boolean*                  ||
|**SimplifiedMat**              |*MaterialInstanceDynamic*  ||
|**Sphere**                     |*SphereComponent*                         ||
|**StandingOrder**              |*String*                   ||
|**TextRender**                 |*TextRenderComponent*      ||


## Functions
[**ConstructionScript**](../../Methods/ClientMethods/ConstructionScript_SwarmGroup.md)  
[**GetUnit**](../../Methods/ClientMethods/GetUnit.md)  
[**ProcessStandingOrder**](../../Methods/ClientMethods/ProcessStandingOrder.md)  
[**SetDebugText**](../../Methods/ClientMethods/SetDebugText.md)  

## Events
[**AddUnit**](../../Events/AddUnit.md)  
[**ArrivedEvent**](../../Events/ArrivedEvent_SwarmGroup.md)  
[**AttackUnit**](../../Events/AttackUnit.md)  
[**CalcHealth**](../../Events/CalcHealth.md)  
[**DestroyUnit**](../../Events/DestroyUnit.md)  
[**Event BeginPlay**](../../Events/BeginPlay_SwarmGroup.md)  
[**Event Tick**](../../Events/Tick_SwarmGroup.md)  
[**InitializeBlankGroup**](../../Events/InitializeBlankGroup.md)  
[**InitializeGroup**](../../Events/InitializeGroup.md)  
[**InTransit**](../../Events/InTransit.md)  
[**MoveOnSpline**](../../Events/MoveOnSpline.md)  
[**MoveOrder**](../../Events/MoveOrder.md)  
[**On Component Begin Overlap**](../../Events/ComponentBeginOverlap_SwarmGroup.md)  
[**On Component End Overlap**](../../Events/ComponentEndOverlap_SwarmGroup.md)  
[**RdyToMove**](../../Events/RdyToMove.md)  
[**RemoveUnit**](../../Events/RemoveUnit.md)  
[**SetUnitHealth**](../../Events/SetUnitHealth.md)  
[**SplitGroup**](../../Events/SplitGroup.md)  
[**ToggleSwarmVisibility**](../../Events/ToggleSwarmVisibility.md)

## Event Dispatchers
[**AttackCompleted**](../../Dispatchers/AttackCompleted.md)  
[**EventCompleted**](../../Dispatchers/EventCompleted.md)  

## Macros
[**BuildDebugString**](../../Macros/BuildDebugString.md)  
[**CalculateGroupHealth**](../../Macros/CalculateGroupHealth.md)  
[**DebugCreation**](../../Macros/DebugCreation.md)  
[**GetNextMoveChunk_Normal**](../../Macros/GetNextMoveChunk_Normal.md)  
[**GetNextMoveChunk_Spline**](../../Macros/GetNextMoveChunk_Spline.md)  
[**GetRandomAttacker**](../../Macros/GetRandomAttacker.md)  
[**GetRandomUnit**](../../Macros/GetRandomUnit.md)  
[**IncrementalMove**](../../Macros/IncrementalMove.md)  