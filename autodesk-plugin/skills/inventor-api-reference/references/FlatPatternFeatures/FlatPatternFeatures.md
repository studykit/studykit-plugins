# FlatPatternFeatures Object

## Description

The FlatPatternFeatures object represents a collection of FlatPatternFeature objects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CreatePath](../FlatPatternFeatures/FlatPatternFeatures_CreatePath.md) | Method that creates a path used to define the shape of several part features such as sweep, rectangular pattern, split, etc. All other 2D and 3D curves that are connected to the input curve are obtained and used to create a Path object. The new Path is returned. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../FlatPatternFeatures/FlatPatternFeatures_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ChamferFeatures](../FlatPatternFeatures/FlatPatternFeatures_ChamferFeatures.md) | Inventor::PartFeatures::ChamferFeatures |
| [CircularPatternFeatures](../FlatPatternFeatures/FlatPatternFeatures_CircularPatternFeatures.md) | Inventor::SheetMetalFeatures::CornerChamferFeatures |
| [ClientFeatures](../FlatPatternFeatures/FlatPatternFeatures_ClientFeatures.md) | Gets the ClientFeatures object associated with the flat pattern. |
| [CornerChamferFeatures](../FlatPatternFeatures/FlatPatternFeatures_CornerChamferFeatures.md) | Inventor::SheetMetalFeatures::CornerChamferFeatures |
| [CornerRoundFeatures](../FlatPatternFeatures/FlatPatternFeatures_CornerRoundFeatures.md) | Inventor::SheetMetalFeatures::CornerRoundFeatures |
| [CosmeticBendFeatures](../FlatPatternFeatures/FlatPatternFeatures_CosmeticBendFeatures.md) | Returns the CosmeticBendFeatures collection object. |
| [Count](../FlatPatternFeatures/FlatPatternFeatures_Count.md) | Property that returns the number of features in the flat pattern. |
| [CutFeatures](../FlatPatternFeatures/FlatPatternFeatures_CutFeatures.md) | Inventor::SheetMetalFeatures::CutFeatures |
| [EmbossFeatures](../FlatPatternFeatures/FlatPatternFeatures_EmbossFeatures.md) | Inventor::SheetMetalFeatures::EmbossFeatures |
| [ExtrudeFeatures](../FlatPatternFeatures/FlatPatternFeatures_ExtrudeFeatures.md) | Inventor::PartFeatures::ExtrudeFeatures |
| [FilletFeatures](../FlatPatternFeatures/FlatPatternFeatures_FilletFeatures.md) | Inventor::PartFeatures::FilletFeatures |
| [HoleFeatures](../FlatPatternFeatures/FlatPatternFeatures_HoleFeatures.md) | Inventor::PartFeatures::HoleFeatures |
| [iFeatures](../FlatPatternFeatures/FlatPatternFeatures_iFeatures.md) | Inventor::PartFeatures::iFeatures |
| [Item](../FlatPatternFeatures/FlatPatternFeatures_Item.md) | Returns the specified PartFeature object from the collection. This is limited to the features within the flat pattern. |
| [MarkFeatures](../FlatPatternFeatures/FlatPatternFeatures_MarkFeatures.md) | Property that returns the MarkFeature collection object. This collection provides access to existing MarkFeature objects and provides functionality to create new MarkFeature objects. |
| [MirrorFeatures](../FlatPatternFeatures/FlatPatternFeatures_MirrorFeatures.md) | Inventor::PartFeatures::MirrorFeatures |
| [PunchToolFeatures](../FlatPatternFeatures/FlatPatternFeatures_PunchToolFeatures.md) | Inventor::SheetMetalFeatures::PunchToolFeatures |
| [RectangularPatternFeatures](../FlatPatternFeatures/FlatPatternFeatures_RectangularPatternFeatures.md) | Inventor::PartFeatures::RectangularPatternFeatures |
| [RevolveFeatures](../FlatPatternFeatures/FlatPatternFeatures_RevolveFeatures.md) | Inventor::PartFeatures::RevolveFeatures |
| [SketchDrivenPatternFeatures](../FlatPatternFeatures/FlatPatternFeatures_SketchDrivenPatternFeatures.md) | Gets the collection object that besides listing out the subset of part features that are SketchDrivenPatterns, allows the creations of new SketchDrivenPatterns. |
| [SweepFeatures](../FlatPatternFeatures/FlatPatternFeatures_SweepFeatures.md) | Inventor::PartFeatures::SweepFeatures |
| [Type](../FlatPatternFeatures/FlatPatternFeatures_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[FlatPattern.Features](../FlatPattern/FlatPattern_Features.md)

## Version

Introduced in version 2010
