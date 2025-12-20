# LinearModelDimensionDefinition Object

Derived from: [ModelDimensionDefinition](../ModelDimensionDefinition/ModelDimensionDefinition.md) Object

## Description

LinearModelDimensionDefinition Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../LinearModelDimensionDefinition/LinearModelDimensionDefinition_Copy.md) | Method that creates a copy of this LinearModelDimensionDefinition object. The new LinearModelDimensionDefinition object is independent of any dimension. It can edited and used as input to edit an existing dimension or to create a new dimension. |
| [GetInspectionDimensionData](../LinearModelDimensionDefinition/LinearModelDimensionDefinition_GetInspectionDimensionData.md) | Method that returns the data associated with an inspection dimension. This method returns an error if the IsInspectionDimension property returns False. |
| [IsValidAnnotationPlane](../LinearModelDimensionDefinition/LinearModelDimensionDefinition_IsValidAnnotationPlane.md) | Method that returns the wheather a planer object is valid to be used as an annotation plane for this model dimension. |
| [SetInspectionDimensionData](../LinearModelDimensionDefinition/LinearModelDimensionDefinition_SetInspectionDimensionData.md) | Method that sets the data associated with an inspection dimension. This method automatically sets the IsInspectionDimension property to True, if it isn’t already. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AnnotationPlane](../LinearModelDimensionDefinition/LinearModelDimensionDefinition_AnnotationPlane.md) | Read-write property that gets and sets the annotation plane for the dimension. Will return nothing in the case where the ModelDimensionDefinition object is transient and not associated with a dimension. |
| [AnnotationPlaneDefinition](../LinearModelDimensionDefinition/LinearModelDimensionDefinition_AnnotationPlaneDefinition.md) | Read-write property that gets and sets the annotation plane definition for the dimension. |
| [Application](../LinearModelDimensionDefinition/LinearModelDimensionDefinition_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [DimensionType](../LinearModelDimensionDefinition/LinearModelDimensionDefinition_DimensionType.md) | Read-only property that returns the dimension type. Possible values are kAlignedDimensionType, kHorizontalDimensionType, kVerticalDimensionType, kArcLengthDimensionType, kSymmetricDimensionType and kDiametricDimensionType. |
| [FirstArrowheadType](../LinearModelDimensionDefinition/LinearModelDimensionDefinition_FirstArrowheadType.md) | Read-write property that gets and sets the type of the first arrowhead. This is a style override. |
| [IntentOne](../LinearModelDimensionDefinition/LinearModelDimensionDefinition_IntentOne.md) | Read-write property that gets and sets the first geometry associated with the dimension. |
| [IntentTwo](../LinearModelDimensionDefinition/LinearModelDimensionDefinition_IntentTwo.md) | Read-write property that gets and sets the second geometry associated with the dimension. |
| [IsExtensionLineOneVisible](../LinearModelDimensionDefinition/LinearModelDimensionDefinition_IsExtensionLineOneVisible.md) | Read-write property that gets and sets whether the first extension line is visible. |
| [IsExtensionLineTwoVisible](../LinearModelDimensionDefinition/LinearModelDimensionDefinition_IsExtensionLineTwoVisible.md) | Read-write property that gets and sets whether the second extension line is visible. This property returns False and cannot be set to True for linear symmetric dimensions. For linear diametric dimensions, this property returns False and cannot be set to True. |
| [IsFirstArrowheadInside](../LinearModelDimensionDefinition/LinearModelDimensionDefinition_IsFirstArrowheadInside.md) | Read-write property that gets and sets whether the first arrowhead is inside or not. |
| [IsInspectionDimension](../LinearModelDimensionDefinition/LinearModelDimensionDefinition_IsInspectionDimension.md) | Read-write property that gets and sets whether this is an inspection dimension. Inspection dimensions are used during the quality control process. They are formatted specifically to indicate which dimensions must be checked before accepting a part. The dimens. |
| [IsModelValueOverridden](../LinearModelDimensionDefinition/LinearModelDimensionDefinition_IsModelValueOverridden.md) | Read-write property that gets and sets whether the model value is overridden for the dimension. Setting the OverrideModelValue property automatically toggles this property to True. |
| [IsOppositeAngleOfArc](../LinearModelDimensionDefinition/LinearModelDimensionDefinition_IsOppositeAngleOfArc.md) | Read-write property that gets and sets whether the opposite angle of an arc is dimensioned or not. This is only applicable when an arc is dimensioned and the value of this property should be ignored in other cases. |
| [IsSecondArrowheadInside](../LinearModelDimensionDefinition/LinearModelDimensionDefinition_IsSecondArrowheadInside.md) | Read-write property that gets and sets whether the second arrowhead is inside or not. |
| [IsValueHidden](../LinearModelDimensionDefinition/LinearModelDimensionDefinition_IsValueHidden.md) | Read-write property that gets and sets whether to display the dimension value. |
| [OverrideModelValue](../LinearModelDimensionDefinition/LinearModelDimensionDefinition_OverrideModelValue.md) | Read-write property that gets and sets the display value for the dimension. |
| [Parent](../LinearModelDimensionDefinition/LinearModelDimensionDefinition_Parent.md) | Read-only property that returns the parent model annotation that the definition is associated with. This property will return Nothing in the case where the definition is not associated with any annotation. This is the case when it’s been created using one of the create definition methods and when it’s been copied from another definition object. |
| [Precision](../LinearModelDimensionDefinition/LinearModelDimensionDefinition_Precision.md) | Read-write property that gets and sets the number of decimal places displayed for this dimension. Values are truncated and rounded to the specified precision. Valid range of values is 0 to 8. |
| [SecondArrowheadType](../LinearModelDimensionDefinition/LinearModelDimensionDefinition_SecondArrowheadType.md) | Read-write property that gets and sets the type of the second arrowhead. This is a style override. This property returns an error and cannot be set for the following dimension types: radius dimensions, diameter dimensions with the SingleDimensionLine property. |
| [Text](../LinearModelDimensionDefinition/LinearModelDimensionDefinition_Text.md) | Read-only property that gets the text of the dimension. Properties on the returned ModelAnnotationText object can be edited to change the displayed text. |
| [TextPosition](../LinearModelDimensionDefinition/LinearModelDimensionDefinition_TextPosition.md) | Read-write property that controls the position of the dimension text. When being set, the input point will be projected onto the orientation plane. |
| [Tolerance](../LinearModelDimensionDefinition/LinearModelDimensionDefinition_Tolerance.md) | Read-only property that returns the Tolerance object associated with this dimension. Methods and properties on the returned Tolerance object can be used to add/edit tolerance information for the dimension. |
| [TolerancePrecision](../LinearModelDimensionDefinition/LinearModelDimensionDefinition_TolerancePrecision.md) | Read-write property that gets and sets the number of decimal places displayed for this dimension tolerance. Values are truncated and rounded to the specified precision. Valid range of values is 0 to 8. |
| [Type](../LinearModelDimensionDefinition/LinearModelDimensionDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[LinearModelDimensionDefinition.Copy](../LinearModelDimensionDefinition/LinearModelDimensionDefinition_Copy.md), [LinearModelDimensions.CreateDefinition](../LinearModelDimensions/LinearModelDimensions_CreateDefinition.md)

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |