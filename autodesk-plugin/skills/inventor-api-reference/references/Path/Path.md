# Path Object

## Description

The Path object represents a single set of connected curves. The order of the objects within the collection is the same as the connection order of the entities.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetReferenceKey](../Path/Path_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../Path/Path_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../Path/Path_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Closed](../Path/Path_Closed.md) | Property that returns a Boolean indicating if the path is closed or not. Returns True in the case of a closed path. |
| [Count](../Path/Path_Count.md) | Property that returns the number of items in this collection. |
| [Item](../Path/Path_Item.md) | Returns the specified PathEntity object from the collection. |
| [Type](../Path/Path_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Wires](../Path/Path_Wires.md) | Property returning the Wires collection object associated with this Path. |

## Accessed From

[ContourFlangeDefinition.Path](../ContourFlangeDefinition/ContourFlangeDefinition_Path.md), [Features.CreatePath](../Features/Features_CreatePath.md), [Features.CreateSpecifiedPath](../Features/Features_CreateSpecifiedPath.md), [FlatPatternFeatures.CreatePath](../FlatPatternFeatures/FlatPatternFeatures_CreatePath.md), [LoftedFlangeDefinition.ProfileOne](../LoftedFlangeDefinition/LoftedFlangeDefinition_ProfileOne.md), [LoftedFlangeDefinition.ProfileTwo](../LoftedFlangeDefinition/LoftedFlangeDefinition_ProfileTwo.md), [PartFeatures.CreatePath](../PartFeatures/PartFeatures_CreatePath.md), [PartFeatures.CreateSpecifiedPath](../PartFeatures/PartFeatures_CreateSpecifiedPath.md), [PathAndGuideRailSweepDef.GuideRail](PathAndGuideRailSweepDef_GuideRail.md), [PathEntity.Parent](../PathEntity/PathEntity_Parent.md), [PathEntityProxy.Parent](../PathEntityProxy/PathEntityProxy_Parent.md), [PathProxy.NativeObject](../PathProxy/PathProxy_NativeObject.md), [SheetMetalFeatures.CreatePath](../SheetMetalFeatures/SheetMetalFeatures_CreatePath.md), [SheetMetalFeatures.CreateSpecifiedPath](../SheetMetalFeatures/SheetMetalFeatures_CreateSpecifiedPath.md), [SolidSweepDefinition.Path](../SolidSweepDefinition/SolidSweepDefinition_Path.md), [SweepDefinition.GuideRail](../SweepDefinition/SweepDefinition_GuideRail.md), [SweepDefinition.Path](../SweepDefinition/SweepDefinition_Path.md)

## Derived Classes

[PathProxy](../PathProxy/PathProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal lofted flange feature](../../sample-programs/LoftedFlangeFeatures_Add_Sample.md) | The following sample demonstrates the creation of a sheet metal lofted flange feature. |
| [Sweep Feature Add](../../sample-programs/SweepFeature_Sample.md) | This sample demonstrates the creation of a sweep feature. The profile is a circle, but the path is made up of a 3D sketch and a 2D sketch. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |