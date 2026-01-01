# HoleFeatures Object

## Description

The HoleFeatures object provides access to all of the objects in a component definition and provides methods to create additional HoleFeature objects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddCBoreByDistanceExtent2](../HoleFeatures/HoleFeatures_AddCBoreByDistanceExtent2.md) | Method that creates a new counterbore HoleFeature using distance extents. The new HoleFeature is returned. |
| [AddCBoreByThroughAllExtent](../HoleFeatures/HoleFeatures_AddCBoreByThroughAllExtent.md) | Method that creates a new counterbore HoleFeature using 'through all' extents. The new HoleFeature is returned. |
| [AddCBoreByToFaceExtent2](../HoleFeatures/HoleFeatures_AddCBoreByToFaceExtent2.md) | Method that creates a new counterbore HoleFeature using 'to face' extents. The new HoleFeature is returned. |
| [AddCSinkByDistanceExtent2](../HoleFeatures/HoleFeatures_AddCSinkByDistanceExtent2.md) | Method that creates a new countersink HoleFeature using distance extents. The new HoleFeature is returned. |
| [AddCSinkByThroughAllExtent](../HoleFeatures/HoleFeatures_AddCSinkByThroughAllExtent.md) | Method that creates a new counter sink HoleFeature using 'through all' extents. The new HoleFeature is returned. |
| [AddCSinkByToFaceExtent2](../HoleFeatures/HoleFeatures_AddCSinkByToFaceExtent2.md) | Method that creates a new countersink HoleFeature using 'to face' extents. The new HoleFeature is returned. |
| [AddDrilledByDistanceExtent2](../HoleFeatures/HoleFeatures_AddDrilledByDistanceExtent2.md) | Method that creates a new drilled HoleFeature using distance extents. The new HoleFeature is returned. |
| [AddDrilledByThroughAllExtent](../HoleFeatures/HoleFeatures_AddDrilledByThroughAllExtent.md) | Method that creates a new drilled HoleFeature using 'through all' extents. The new HoleFeature is returned. |
| [AddDrilledByToFaceExtent2](../HoleFeatures/HoleFeatures_AddDrilledByToFaceExtent2.md) | Method that creates a new drilled HoleFeature using 'to face' extents. The new HoleFeature is returned. |
| [AddSpotFaceByDistanceExtent2](../HoleFeatures/HoleFeatures_AddSpotFaceByDistanceExtent2.md) | Creates a new SpotFace HoleFeature using distance extents. |
| [AddSpotFaceByThroughAllExtent](../HoleFeatures/HoleFeatures_AddSpotFaceByThroughAllExtent.md) | Method that creates a new spotface HoleFeature using 'through all' extents. The new HoleFeature is returned. |
| [AddSpotFaceByToFaceExtent2](../HoleFeatures/HoleFeatures_AddSpotFaceByToFaceExtent2.md) | Creates a new SpotFace HoleFeature using to face extents. |
| [CreateClearanceInfo](../HoleFeatures/HoleFeatures_CreateClearanceInfo.md) | Creates a new ClearanceInfo object. |
| [CreatePointPlacementDefinition](../HoleFeatures/HoleFeatures_CreatePointPlacementDefinition.md) | Method that creates a new PointHolePlacementDefinition object that can be used for defining the placement of Hole features coincident with a work point and positioned with respect to an axis, edge or work plane. |
| [CreateSketchPlacementDefinition](../HoleFeatures/HoleFeatures_CreateSketchPlacementDefinition.md) | Method that creates a new SketchHolePlacementDefinition object that can be used for defining the placement of Hole features using sketch points. |
| [CreateTaperedTapInfo](../HoleFeatures/HoleFeatures_CreateTaperedTapInfo.md) | Method that creates a new TaperedThreadInfo object that can be used in creating HoleFeature objects. See the Thread.xls file that is delivered with Inventor for examples of valid input for these arguments. The spreadsheet columns match one for one with these arguments. |
| [CreateTapInfo](../HoleFeatures/HoleFeatures_CreateTapInfo.md) | Method that creates a new HoleTapInfo object that can be used in creating threads for Hole features. See the Thread.xls file that is delivered with Autodesk Inventor for examples of valid input for these arguments. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../HoleFeatures/HoleFeatures_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../HoleFeatures/HoleFeatures_Count.md) | Property that returns the number of items in this collection. |
| [Item](../HoleFeatures/HoleFeatures_Item.md) | Returns the specified HoleFeature object from the collection. This is the default property of the HoleFeatures collection object. |
| [Type](../HoleFeatures/HoleFeatures_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Features.HoleFeatures](../Features/Features_HoleFeatures.md), [FlatPatternFeatures.HoleFeatures](../FlatPatternFeatures/FlatPatternFeatures_HoleFeatures.md), [PartFeatures.HoleFeatures](../PartFeatures/PartFeatures_HoleFeatures.md), [SheetMetalFeatures.HoleFeatures](../SheetMetalFeatures/SheetMetalFeatures_HoleFeatures.md)

## Version

Introduced in version 5
