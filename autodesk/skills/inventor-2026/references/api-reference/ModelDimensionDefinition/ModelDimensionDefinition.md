# ModelDimensionDefinition Object

## Description

The ModelDimensionDefinition object is the base class for all model dimension definitions in a part or assembly.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetInspectionDimensionData](../ModelDimensionDefinition/ModelDimensionDefinition_GetInspectionDimensionData.md) | Method that returns the data associated with an inspection dimension. This method returns an error if the IsInspectionDimension property returns False. |
| [IsValidAnnotationPlane](../ModelDimensionDefinition/ModelDimensionDefinition_IsValidAnnotationPlane.md) | Method that returns the wheather a planer object is valid to be used as an annotation plane for this model dimension. |
| [SetInspectionDimensionData](../ModelDimensionDefinition/ModelDimensionDefinition_SetInspectionDimensionData.md) | Method that sets the data associated with an inspection dimension. This method automatically sets the IsInspectionDimension property to True, if it isn’t already. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AnnotationPlane](../ModelDimensionDefinition/ModelDimensionDefinition_AnnotationPlane.md) | Read-write property that gets and sets the annotation plane for the dimension. Will return nothing in the case where the ModelDimensionDefinition object is transient and not associated with a dimension. |
| [AnnotationPlaneDefinition](../ModelDimensionDefinition/ModelDimensionDefinition_AnnotationPlaneDefinition.md) | Read-write property that gets and sets the annotation plane definition for the dimension. |
| [Application](../ModelDimensionDefinition/ModelDimensionDefinition_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [IsInspectionDimension](../ModelDimensionDefinition/ModelDimensionDefinition_IsInspectionDimension.md) | Read-write property that gets and sets whether this is an inspection dimension. Inspection dimensions are used during the quality control process. They are formatted specifically to indicate which dimensions must be checked before accepting a part. The dimens. |
| [IsModelValueOverridden](../ModelDimensionDefinition/ModelDimensionDefinition_IsModelValueOverridden.md) | Read-write property that gets and sets whether the model value is overridden for the dimension. Setting the OverrideModelValue property automatically toggles this property to True. |
| [IsValueHidden](../ModelDimensionDefinition/ModelDimensionDefinition_IsValueHidden.md) | Read-write property that gets and sets whether to display the dimension value. |
| [OverrideModelValue](../ModelDimensionDefinition/ModelDimensionDefinition_OverrideModelValue.md) | Read-write property that gets and sets the display value for the dimension. |
| [Parent](../ModelDimensionDefinition/ModelDimensionDefinition_Parent.md) | Read-only property that returns the parent model annotation that the definition is associated with. This property will return Nothing in the case where the definition is not associated with any annotation. This is the case when it’s been created using one of the create definition methods and when it’s been copied from another definition object. |
| [Precision](../ModelDimensionDefinition/ModelDimensionDefinition_Precision.md) | Read-write property that gets and sets the number of decimal places displayed for this dimension. Values are truncated and rounded to the specified precision. Valid range of values is 0 to 8. |
| [Text](../ModelDimensionDefinition/ModelDimensionDefinition_Text.md) | Read-only property that gets the text of the dimension. Properties on the returned ModelAnnotationText object can be edited to change the displayed text. |
| [TextPosition](../ModelDimensionDefinition/ModelDimensionDefinition_TextPosition.md) | Read-write property that controls the position of the dimension text. When being set, the input point will be projected onto the orientation plane. |
| [Tolerance](../ModelDimensionDefinition/ModelDimensionDefinition_Tolerance.md) | Read-only property that returns the Tolerance object associated with this dimension. Methods and properties on the returned Tolerance object can be used to add/edit tolerance information for the dimension. |
| [TolerancePrecision](../ModelDimensionDefinition/ModelDimensionDefinition_TolerancePrecision.md) | Read-write property that gets and sets the number of decimal places displayed for this dimension tolerance. Values are truncated and rounded to the specified precision. Valid range of values is 0 to 8. |
| [Type](../ModelDimensionDefinition/ModelDimensionDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[AngularModelDimension.Definition](../AngularModelDimension/AngularModelDimension_Definition.md), [AngularModelDimensionProxy.Definition](../AngularModelDimensionProxy/AngularModelDimensionProxy_Definition.md), [DiameterModelDimension.Definition](../DiameterModelDimension/DiameterModelDimension_Definition.md), [DiameterModelDimensionProxy.Definition](../DiameterModelDimensionProxy/DiameterModelDimensionProxy_Definition.md), [LinearModelDimension.Definition](../LinearModelDimension/LinearModelDimension_Definition.md), [LinearModelDimensionProxy.Definition](../LinearModelDimensionProxy/LinearModelDimensionProxy_Definition.md), [ModelDimension.Definition](../ModelDimension/ModelDimension_Definition.md), [RadiusModelDimension.Definition](../RadiusModelDimension/RadiusModelDimension_Definition.md), [RadiusModelDimensionProxy.Definition](../RadiusModelDimensionProxy/RadiusModelDimensionProxy_Definition.md)

## Derived Classes

[AngularModelDimensionDefinition](../AngularModelDimensionDefinition/AngularModelDimensionDefinition.md), [DiameterModelDimensionDefinition](../DiameterModelDimensionDefinition/DiameterModelDimensionDefinition.md), [LinearModelDimensionDefinition](../LinearModelDimensionDefinition/LinearModelDimensionDefinition.md), [RadiusModelDimensionDefinition](../RadiusModelDimensionDefinition/RadiusModelDimensionDefinition.md)

## Version

Introduced in version 2018
