# DiameterModelDimensionDefinition Object

Derived from: [ModelDimensionDefinition](../ModelDimensionDefinition/ModelDimensionDefinition.md) Object

## Description

The DiameterModelDimensionDefinition provides access to all of the information that defines a diameter model dimension. It is derived from the ModelDimensionDefinition object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../DiameterModelDimensionDefinition/DiameterModelDimensionDefinition_Copy.md) | Method that creates a copy of this DiameterModelDimensionDefinition object. The new DiameterModelDimensionDefinition object is independent of any dimension. It can edited and used as input to edit an existing dimension or to create a new dimension. |
| [GetInspectionDimensionData](../DiameterModelDimensionDefinition/DiameterModelDimensionDefinition_GetInspectionDimensionData.md) | Method that returns the data associated with an inspection dimension. This method returns an error if the IsInspectionDimension property returns False. |
| [IsValidAnnotationPlane](../DiameterModelDimensionDefinition/DiameterModelDimensionDefinition_IsValidAnnotationPlane.md) | Method that returns the wheather a planer object is valid to be used as an annotation plane for this model dimension. |
| [SetInspectionDimensionData](../DiameterModelDimensionDefinition/DiameterModelDimensionDefinition_SetInspectionDimensionData.md) | Method that sets the data associated with an inspection dimension. This method automatically sets the IsInspectionDimension property to True, if it isn’t already. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AnnotationPlane](../DiameterModelDimensionDefinition/DiameterModelDimensionDefinition_AnnotationPlane.md) | Read-write property that gets and sets the annotation plane for the dimension. Will return nothing in the case where the ModelDimensionDefinition object is transient and not associated with a dimension. |
| [AnnotationPlaneDefinition](../DiameterModelDimensionDefinition/DiameterModelDimensionDefinition_AnnotationPlaneDefinition.md) | Read-write property that gets and sets the annotation plane definition for the dimension. |
| [Application](../DiameterModelDimensionDefinition/DiameterModelDimensionDefinition_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [ArrowheadType](../DiameterModelDimensionDefinition/DiameterModelDimensionDefinition_ArrowheadType.md) | Read-write property that gets and sets the type of the first arrowhead. This is a style override. |
| [Intent](../DiameterModelDimensionDefinition/DiameterModelDimensionDefinition_Intent.md) | Read-write property that gets and sets the first geometry associated with the dimension. |
| [IsArrowheadsInside](../DiameterModelDimensionDefinition/DiameterModelDimensionDefinition_IsArrowheadsInside.md) | Read-write property that gets and sets whether the arrowheads are inside or outside. |
| [IsInspectionDimension](../DiameterModelDimensionDefinition/DiameterModelDimensionDefinition_IsInspectionDimension.md) | Read-write property that gets and sets whether this is an inspection dimension. Inspection dimensions are used during the quality control process. They are formatted specifically to indicate which dimensions must be checked before accepting a part. The dimens. |
| [IsLeaderFromCenter](../DiameterModelDimensionDefinition/DiameterModelDimensionDefinition_IsLeaderFromCenter.md) | Read-write property that gets and sets whether the leader starts from the center of the arc or the circle. |
| [IsModelValueOverridden](../DiameterModelDimensionDefinition/DiameterModelDimensionDefinition_IsModelValueOverridden.md) | Read-write property that gets and sets whether the model value is overridden for the dimension. Setting the OverrideModelValue property automatically toggles this property to True. |
| [IsValueHidden](../DiameterModelDimensionDefinition/DiameterModelDimensionDefinition_IsValueHidden.md) | Read-write property that gets and sets whether to display the dimension value. |
| [LandingPosition](../DiameterModelDimensionDefinition/DiameterModelDimensionDefinition_LandingPosition.md) | Read-write property that gets and sets the landing position of the dimension. The point is projected onto the orientation plane. |
| [OverrideModelValue](../DiameterModelDimensionDefinition/DiameterModelDimensionDefinition_OverrideModelValue.md) | Read-write property that gets and sets the display value for the dimension. |
| [Parent](../DiameterModelDimensionDefinition/DiameterModelDimensionDefinition_Parent.md) | Read-only property that returns the parent model annotation that the definition is associated with. This property will return Nothing in the case where the definition is not associated with any annotation. This is the case when it’s been created using one of the create definition methods and when it’s been copied from another definition object. |
| [Precision](../DiameterModelDimensionDefinition/DiameterModelDimensionDefinition_Precision.md) | Read-write property that gets and sets the number of decimal places displayed for this dimension. Values are truncated and rounded to the specified precision. Valid range of values is 0 to 8. |
| [Text](../DiameterModelDimensionDefinition/DiameterModelDimensionDefinition_Text.md) | Read-only property that gets the text of the dimension. Properties on the returned ModelAnnotationText object can be edited to change the displayed text. |
| [TextPosition](../DiameterModelDimensionDefinition/DiameterModelDimensionDefinition_TextPosition.md) | Read-write property that controls the position of the dimension text. When being set, the input point will be projected onto the orientation plane. |
| [Tolerance](../DiameterModelDimensionDefinition/DiameterModelDimensionDefinition_Tolerance.md) | Read-only property that returns the Tolerance object associated with this dimension. Methods and properties on the returned Tolerance object can be used to add/edit tolerance information for the dimension. |
| [TolerancePrecision](../DiameterModelDimensionDefinition/DiameterModelDimensionDefinition_TolerancePrecision.md) | Read-write property that gets and sets the number of decimal places displayed for this dimension tolerance. Values are truncated and rounded to the specified precision. Valid range of values is 0 to 8. |
| [Type](../DiameterModelDimensionDefinition/DiameterModelDimensionDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DiameterModelDimensionDefinition.Copy](../DiameterModelDimensionDefinition/DiameterModelDimensionDefinition_Copy.md), [DiameterModelDimensions.CreateDefinition](../DiameterModelDimensions/DiameterModelDimensions_CreateDefinition.md)

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |