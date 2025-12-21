# GeometryIntent Object

## Description

The GeometryIntent object represents a geometry intent for use in various annotation and view creations.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../GeometryIntent/GeometryIntent_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Geometry](../GeometryIntent/GeometryIntent_Geometry.md) | Property that returns the geometry associated with the intent. |
| [Intent](../GeometryIntent/GeometryIntent_Intent.md) | Property that returns the intent point on the input geometry. This can be a value from PointIntentEnum, a geometry if the intent is the intersection of two geometries, a Point2d object that specifies a sheet point on the geometry or a double value indicating the parameter on the input curve geometry. |
| [IntentType](../GeometryIntent/GeometryIntent_IntentType.md) | Property that returns intent type indicating the type of value that the Intent property will return. Possible return values are kPointEnumIntent (a PointIntentEnum will be returned), kPoint2dIntent (a Point2d object will be returned), kParameterIntent (a double value will be returned), kGeometryIntent (a DrawingCurve or a SketchEntity will be returned) or kNoPointIntent (the GeometryIntent is not a point and the Intent property will not return a meaningful value). |
| [Parent](../GeometryIntent/GeometryIntent_Parent.md) | Property that returns the parent of this object. |
| [Point](../GeometryIntent/GeometryIntent_Point.md) | Read-only property that returns a 3d point define by the geometry intent. This property returns nothing there is not a 3d point intent. |
| [PointOnSheet](../GeometryIntent/GeometryIntent_PointOnSheet.md) | Property that returns the point on sheet represented by a point intent. This property returns Nothing if this is not a point intent. |
| [Type](../GeometryIntent/GeometryIntent_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[AngularGeneralDimension.IntentOne](../AngularGeneralDimension/AngularGeneralDimension_IntentOne.md), [AngularGeneralDimension.IntentThree](../AngularGeneralDimension/AngularGeneralDimension_IntentThree.md), [AngularGeneralDimension.IntentTwo](../AngularGeneralDimension/AngularGeneralDimension_IntentTwo.md), [AngularModelDimensionDefinition.IntentOne](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_IntentOne.md), [AngularModelDimensionDefinition.IntentThree](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_IntentThree.md), [AngularModelDimensionDefinition.IntentTwo](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_IntentTwo.md), [AssemblyComponentDefinition.CreateGeometryIntent](../AssemblyComponentDefinition/AssemblyComponentDefinition_CreateGeometryIntent.md), [AssemblyJointDefinition.OriginOne](../AssemblyJointDefinition/AssemblyJointDefinition_OriginOne.md), [AssemblyJointDefinition.OriginTwo](../AssemblyJointDefinition/AssemblyJointDefinition_OriginTwo.md), [BaselineDimensionSet.Origin](../BaselineDimensionSet/BaselineDimensionSet_Origin.md), [Centerline.GetBisectorEntities](../Centerline/Centerline_GetBisectorEntities.md), [Centerline.PatternCenter](../Centerline/Centerline_PatternCenter.md), [DetailDrawingView.AttachPoint](../DetailDrawingView/DetailDrawingView_AttachPoint.md), [DiameterGeneralDimension.Intent](../DiameterGeneralDimension/DiameterGeneralDimension_Intent.md), [DiameterModelDimensionDefinition.Intent](../DiameterModelDimensionDefinition/DiameterModelDimensionDefinition_Intent.md), [FlatPattern.CreateGeometryIntent](../FlatPattern/FlatPattern_CreateGeometryIntent.md), [HoleThreadNote.Intent](../HoleThreadNote/HoleThreadNote_Intent.md), [LeaderNode.AttachedEntity](../LeaderNode/LeaderNode_AttachedEntity.md), [LinearGeneralDimension.IntentOne](../LinearGeneralDimension/LinearGeneralDimension_IntentOne.md), [LinearGeneralDimension.IntentThree](../LinearGeneralDimension/LinearGeneralDimension_IntentThree.md), [LinearGeneralDimension.IntentTwo](../LinearGeneralDimension/LinearGeneralDimension_IntentTwo.md), [LinearGeneralDimension.VirtualArcPosition](../LinearGeneralDimension/LinearGeneralDimension_VirtualArcPosition.md), [LinearModelDimensionDefinition.IntentOne](../LinearModelDimensionDefinition/LinearModelDimensionDefinition_IntentOne.md), [LinearModelDimensionDefinition.IntentTwo](../LinearModelDimensionDefinition/LinearModelDimensionDefinition_IntentTwo.md), [ModelDatumIdentifierDefinition.Intent](../ModelDatumIdentifierDefinition/ModelDatumIdentifierDefinition_Intent.md), [ModelFeatureControlFrameDefinition.Intent](../ModelFeatureControlFrameDefinition/ModelFeatureControlFrameDefinition_Intent.md), [ModelGeneralNoteDefinition.Intent](../ModelGeneralNoteDefinition/ModelGeneralNoteDefinition_Intent.md), [ModelHoleThreadNoteDefinition.Intent](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition_Intent.md), [ModelLeaderNode.Intent](../ModelLeaderNode/ModelLeaderNode_Intent.md), [ModelLeaderNoteDefinition.Intent](../ModelLeaderNoteDefinition/ModelLeaderNoteDefinition_Intent.md), [ModelSurfaceTextureSymbolDefinition.Intent](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_Intent.md), [ModelWeldingSymbolDefinitions.Intent](../ModelWeldingSymbolDefinitions/ModelWeldingSymbolDefinitions_Intent.md), [OrdinateDimension.Intent](../OrdinateDimension/OrdinateDimension_Intent.md), [OriginIndicator.Intent](../OriginIndicator/OriginIndicator_Intent.md), [PartComponentDefinition.CreateGeometryIntent](../PartComponentDefinition/PartComponentDefinition_CreateGeometryIntent.md), [Publication.CreateGeometryIntent](Publication_CreateGeometryIntent.md), [PublicationTrail.Origin](PublicationTrail_Origin.md), [PublicationTrailSegment.Origin](PublicationTrailSegment_Origin.md), [PublicationTweakDefinition.TriadOrigin](PublicationTweakDefinition_TriadOrigin.md), [PublicationTweaks.TriadOrigin](PublicationTweaks_TriadOrigin.md), [PunchNote.PunchEdge](../PunchNote/PunchNote_PunchEdge.md), [RadiusGeneralDimension.Intent](../RadiusGeneralDimension/RadiusGeneralDimension_Intent.md), [RadiusModelDimensionDefinition.Intent](../RadiusModelDimensionDefinition/RadiusModelDimensionDefinition_Intent.md), [Sheet.CreateGeometryIntent](../Sheet/Sheet_CreateGeometryIntent.md), [SheetMetalComponentDefinition.CreateGeometryIntent](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_CreateGeometryIntent.md), [WeldmentComponentDefinition.CreateGeometryIntent](../WeldmentComponentDefinition/WeldmentComponentDefinition_CreateGeometryIntent.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Creation a balloon](../../sample-programs/Balloons_Add_Sample.md) | This sample demonstrates the creation of a balloon. |
| [Baseline dimension sets](../../sample-programs/BaselineDimensionSets_Add_Sample.md) | This sample demonstrates the creation of a baseline set dimension in a drawing. |
| [Chain dimensions sets](../../sample-programs/ChainDimensionSets_Add_Sample.md) | This sample demonstrates the creation of a chain dimension set in a drawing. |
| [Creating hole tables](../../sample-programs/HoleTables_Add_Sample.md) | This sample demonstrates the creation of hole tables in a drawing. |
| [create punch note](../../sample-programs/PunchNotes_Add_Sample.md) | This sample demonstrates the creation of a punch note on the drawing view of a flat pattern. |
| [Create sketched symbol and leader](../../sample-programs/SketchedSymbols_AddWithLeader_Sample.md) | This sample illustrates creating sketched symbol with a leader. |
| [Add surface texture symbol to dimension](../../sample-programs/SurfaceTextureSymbols_Add_Sample.md) | This sample demonstrates the creation of a surface texture symbol attached to the extension line of a drawing dimension. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |