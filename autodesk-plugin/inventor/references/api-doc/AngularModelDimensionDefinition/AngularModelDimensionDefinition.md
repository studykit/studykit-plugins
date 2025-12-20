# AngularModelDimensionDefinition Object

Derived from: [ModelDimensionDefinition](../ModelDimensionDefinition/ModelDimensionDefinition.md) Object

## Description

The AngularModelDimensionDefinition provides access to all of the information that defines a angular model dimension. It is derived from the ModelDimensionDefinition object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_Copy.md) | Method that creates a copy of this AngularModelDimensionDefinition object. The new AngularModelDimensionDefinition object is independent of any dimension. It can edited and used as input to edit an existing dimension or to create a new dimension. |
| [GetInspectionDimensionData](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_GetInspectionDimensionData.md) | Method that returns the data associated with an inspection dimension. This method returns an error if the IsInspectionDimension property returns False. |
| [IsValidAnnotationPlane](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_IsValidAnnotationPlane.md) | Method that returns the wheather a planer object is valid to be used as an annotation plane for this model dimension. |
| [SetInspectionDimensionData](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_SetInspectionDimensionData.md) | Method that sets the data associated with an inspection dimension. This method automatically sets the IsInspectionDimension property to True, if it isn’t already. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AnnotationPlane](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_AnnotationPlane.md) | Read-write property that gets and sets the annotation plane for the dimension. Will return nothing in the case where the ModelDimensionDefinition object is transient and not associated with a dimension. |
| [AnnotationPlaneDefinition](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_AnnotationPlaneDefinition.md) | Read-write property that gets and sets the annotation plane definition for the dimension. |
| [Application](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [ArrowheadsInside](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_ArrowheadsInside.md) | Read-write property that gets and sets whether the arrowheads are inside or outside. This is a style override. |
| [FirstArrowheadType](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_FirstArrowheadType.md) | Read-write property that gets and sets the type of the first arrowhead. This is a style override. |
| [IntentOne](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_IntentOne.md) | Read-write property that gets and sets the first geometry associated with the dimension. |
| [IntentThree](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_IntentThree.md) | Read-write property that gets and sets the third geometry associated with the dimension. |
| [IntentTwo](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_IntentTwo.md) | Read-write property that gets and sets the second geometry associated with the dimension. |
| [IsExtensionLineOneVisible](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_IsExtensionLineOneVisible.md) | Read-write property that gets and sets whether the first extension line is visible. |
| [IsExtensionLineTwoVisible](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_IsExtensionLineTwoVisible.md) | Read-write property that gets and sets whether the second extension line is visible. This property returns False and cannot be set to True for Angular symmetric dimensions. For Angular diametric dimensions, this property returns False and cannot be set to Tr. |
| [IsFirstArrowheadInside](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_IsFirstArrowheadInside.md) | Read-write property that gets and sets whether the first arrowhead is inside or not. |
| [IsInspectionDimension](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_IsInspectionDimension.md) | Read-write property that gets and sets whether this is an inspection dimension. Inspection dimensions are used during the quality control process. They are formatted specifically to indicate which dimensions must be checked before accepting a part. The dimens. |
| [IsModelValueOverridden](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_IsModelValueOverridden.md) | Read-write property that gets and sets whether the model value is overridden for the dimension. Setting the OverrideModelValue property automatically toggles this property to True. |
| [IsSecondArrowheadInside](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_IsSecondArrowheadInside.md) | Read-write property that gets and sets whether the second arrowhead is inside or not. |
| [IsValueHidden](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_IsValueHidden.md) | Read-write property that gets and sets whether to display the dimension value. |
| [OppositeAngle](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_OppositeAngle.md) | Read-write that property that indicates that indicates whether to dimension the opposite angle. This property defaults to False for a newly created AngularModelDimension object. |
| [OverrideModelValue](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_OverrideModelValue.md) | Read-write property that gets and sets the display value for the dimension. |
| [Parent](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_Parent.md) | Read-only property that returns the parent model annotation that the definition is associated with. This property will return Nothing in the case where the definition is not associated with any annotation. This is the case when it’s been created using one of the create definition methods and when it’s been copied from another definition object. |
| [Precision](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_Precision.md) | Read-write property that gets and sets the number of decimal places displayed for this dimension. Values are truncated and rounded to the specified precision. Valid range of values is 0 to 8. |
| [SecondArrowheadType](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_SecondArrowheadType.md) | Read-write property that gets and sets the type of the second arrowhead. This is a style override. This property returns an error and cannot be set for the following dimension types: radius dimensions, diameter dimensions with the SingleDimensionLine property. |
| [Text](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_Text.md) | Read-only property that gets the text of the dimension. Properties on the returned ModelAnnotationText object can be edited to change the displayed text. |
| [TextPosition](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_TextPosition.md) | Read-write property that controls the position of the dimension text. When being set, the input point will be projected onto the orientation plane. |
| [Tolerance](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_Tolerance.md) | Read-only property that returns the Tolerance object associated with this dimension. Methods and properties on the returned Tolerance object can be used to add/edit tolerance information for the dimension. |
| [TolerancePrecision](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_TolerancePrecision.md) | Read-write property that gets and sets the number of decimal places displayed for this dimension tolerance. Values are truncated and rounded to the specified precision. Valid range of values is 0 to 8. |
| [Type](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UseQuadrant](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_UseQuadrant.md) | Read-write that property that indicates whether to use the quadrant in which the input text point lies to decide which angle to dimension. This property defaults to True for a newly created AngularModelDimension object. |

## Accessed From

[AngularModelDimensionDefinition.Copy](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_Copy.md), [AngularModelDimensions.CreateDefinition](../AngularModelDimensions/AngularModelDimensions_CreateDefinition.md)

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |