# FoldDefinition Object

## Description

The FoldDefinition object represents all of the information that defines a fold feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../FoldDefinition/FoldDefinition_Copy.md) | Function that creates a copy of this FoldDefinition object. The copy is independent of any fold feature and can be edited without affecting anything else. It can then be used as input to edit an existing fold feature or create a new fold feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../FoldDefinition/FoldDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BendAngle](../FoldDefinition/FoldDefinition_BendAngle.md) | Gets and sets the bend angle of a sheet metal fold feature. |
| [BendLine](../FoldDefinition/FoldDefinition_BendLine.md) | Gets and sets the SketchLine object that defines the location of the bend line. |
| [BendLocation](../FoldDefinition/FoldDefinition_BendLocation.md) | Gets and sets the position of the bend with respect to the bend line. |
| [BendOptions](../FoldDefinition/FoldDefinition_BendOptions.md) | Gets and sets the BendOptions object that defines the bend options for this bend feature. |
| [BendRadius](../FoldDefinition/FoldDefinition_BendRadius.md) | Gets and sets the bend radius of a sheet metal fold feature. |
| [IsPositiveBendDirection](../FoldDefinition/FoldDefinition_IsPositiveBendDirection.md) | Gets and sets whether the direction of the fold is in the positive or negative direction. |
| [IsPositiveBendSide](../FoldDefinition/FoldDefinition_IsPositiveBendSide.md) | Gets and sets whether the flip direction is positive or negative. |
| [IsUnfoldMethodOverridden](../FoldDefinition/FoldDefinition_IsUnfoldMethodOverridden.md) | Read-write property that gets and set whether the unfold method has been overridden for this feature. Setting this property to False clears the override. Setting the property to True returns a failure. |
| [Parent](../FoldDefinition/FoldDefinition_Parent.md) | Property that returns the parent FoldFeature object of this FoldDefinition object. |
| [Type](../FoldDefinition/FoldDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UnfoldMethod](../FoldDefinition/FoldDefinition_UnfoldMethod.md) | Gets and sets the UnfoldMethod object that defines how this bend is unfolded. |

## Accessed From

[FoldDefinition.Copy](../FoldDefinition/FoldDefinition_Copy.md), [FoldFeature.Definition](../FoldFeature/FoldFeature_Definition.md), [FoldFeatureProxy.Definition](../FoldFeatureProxy/FoldFeatureProxy_Definition.md), [FoldFeatures.CreateFoldDefinition](../FoldFeatures/FoldFeatures_CreateFoldDefinition.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal face and fold features](../../sample-programs/FoldFeatures_Add_Sample.md) | This sample demonstrates the creation of sheet metal face and fold features. |

## Version

Introduced in version 2009
