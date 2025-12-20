# LoftedFlangeDefinition Object

## Description

The LoftedFlangeDefinition object represents all of the information that defines a lofted flange feature. The LoftedFlangeDefinition object is used in two ways. First it is used as input when creating a lofted flange feature. Second it is used to query and edit existing lofted flange features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../LoftedFlangeDefinition/LoftedFlangeDefinition_Copy.md) | Method that creates a copy of this LoftedFlangeDefinition object. The new LoftedFlangeDefinition object is independent of any feature. It can edited and used as input to edit an existing feature or to create a new lofted flange feature. |
| [SetOutputType](../LoftedFlangeDefinition/LoftedFlangeDefinition_SetOutputType.md) | Method that sets the technique that will be used to calculate the lofted flange. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AffectedBodies](../LoftedFlangeDefinition/LoftedFlangeDefinition_AffectedBodies.md) | Gets and sets the collection of bodies affected by this feature. If this property is not set for multi-body parts, the default solid body is used as the affected body. |
| [Application](../LoftedFlangeDefinition/LoftedFlangeDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BendRadius](../LoftedFlangeDefinition/LoftedFlangeDefinition_BendRadius.md) | Read-write property that provides access to the bend radius of a lofted flange feature. |
| [Converge](../LoftedFlangeDefinition/LoftedFlangeDefinition_Converge.md) | Read-write property that defines whether the corner of the lofted flange should converge. |
| [ExtentDirection](../LoftedFlangeDefinition/LoftedFlangeDefinition_ExtentDirection.md) | Gets and sets the which side of the sketch entities is the direction for the material to be added. |
| [FacetTolerance](../LoftedFlangeDefinition/LoftedFlangeDefinition_FacetTolerance.md) | Property that returns the parameter controlling the tolerance used to calculate the lofted flange. This will return Nothing in the case where the OutputType property returns kDieFormedLoftedFlange and where the LoftedFlangeDefinition object is not associated with an existing lofted flange. |
| [IsUnfoldMethodOverridden](../LoftedFlangeDefinition/LoftedFlangeDefinition_IsUnfoldMethodOverridden.md) | Read-write property that gets and set whether the unfold method has been overridden for this feature. Setting this property to False clears the override. Setting the property to True returns a failure. |
| [Operation](../LoftedFlangeDefinition/LoftedFlangeDefinition_Operation.md) | Gets and sets the type of operation used to add the feature to the model. Valid inputs are kNewBodyOperation, kJoinOperation. |
| [OutputType](../LoftedFlangeDefinition/LoftedFlangeDefinition_OutputType.md) | Property that returns the technique being used to calculate the shape of the lofted flange. To set the output type use the SetOutputType method. |
| [Parent](../LoftedFlangeDefinition/LoftedFlangeDefinition_Parent.md) | Property that returns the parent LoftedFlangeFeature object. |
| [ProfileOne](../LoftedFlangeDefinition/LoftedFlangeDefinition_ProfileOne.md) | Gets and sets the first of two profiles defining the lofted flange. |
| [ProfileTwo](../LoftedFlangeDefinition/LoftedFlangeDefinition_ProfileTwo.md) | Gets and sets the second of two profiles defining the lofted flange. |
| [SheetMetalRule](../LoftedFlangeDefinition/LoftedFlangeDefinition_SheetMetalRule.md) | Read-write property that gets and sets the sheet metal style for the body the feature is in. Set this property is applicable only when the feature is the first feature in a solid body. When set this property the default sheet metal rule will be overridden and. |
| [Type](../LoftedFlangeDefinition/LoftedFlangeDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UnfoldMethod](../LoftedFlangeDefinition/LoftedFlangeDefinition_UnfoldMethod.md) | Gets and set the UnfoldMethod object that defines how the bends associated with this lofted flange feature are unfolded. |
| [UseDefaultSheetMetalRule](../LoftedFlangeDefinition/LoftedFlangeDefinition_UseDefaultSheetMetalRule.md) | Read-write property that gets and sets whether to use the document active sheet metal style for the body the feature is in. Set this property is applicable only when the feature is the first feature in a solid body and this can only be set to True from False. |

## Accessed From

[LoftedFlangeDefinition.Copy](../LoftedFlangeDefinition/LoftedFlangeDefinition_Copy.md), [LoftedFlangeFeature.Definition](../LoftedFlangeFeature/LoftedFlangeFeature_Definition.md), [LoftedFlangeFeatureProxy.Definition](../LoftedFlangeFeatureProxy/LoftedFlangeFeatureProxy_Definition.md), [LoftedFlangeFeatures.CreateLoftedFlangeDefinition](../LoftedFlangeFeatures/LoftedFlangeFeatures_CreateLoftedFlangeDefinition.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal lofted flange feature](../../sample-programs/LoftedFlangeFeatures_Add_Sample.md) | The following sample demonstrates the creation of a sheet metal lofted flange feature. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |