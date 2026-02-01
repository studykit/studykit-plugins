# CustomFeatureParameter Object ![Preview](../images/TestTubeLarge.png)

Derived from: [ModelParameter](ModelParameter.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CustomFeatureParameter.h>

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

## Description

A custom parameter is a parameter that was created as the result of a custom feature being created. It is associated with the custom feature and it's lifetime is the same as the custom feature that owns it.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](CustomFeatureParameter_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteMe](CustomFeatureParameter_deleteMe.htm) | Deletes this ModelParameter. As a general rule, model parameters cannot be deleted because features depend on them. However, there are uncommon workflows where a parameter no longer has any dependents and is not automatically deleted. You can use the isDeletable property to see if the parameter is in this state and can successfully be deleted. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [attributes](CustomFeatureParameter_attributes.htm) | Returns the collection of attributes associated with this face. |
| [comment](CustomFeatureParameter_comment.htm) | The comment associated with this parameter |
| [component](CustomFeatureParameter_component.htm) | Returns the Component containing the ModelParameter. |
| [createdBy](CustomFeatureParameter_createdBy.htm) | Returns the object that created this parameter. For example, a feature, a sketch dimension, or a construction plane. |
| [dependencyParameters](CustomFeatureParameter_dependencyParameters.htm) | Returns a list of parameters that this parameter is dependent on. |
| [dependentParameters](CustomFeatureParameter_dependentParameters.htm) | Returns a list of parameters that are dependent on this parameter as a result of this parameter being referenced in their equation. |
| [entityToken](CustomFeatureParameter_entityToken.htm) | Returns a token for the Parameter object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same parameter. |
| [expression](CustomFeatureParameter_expression.htm) | Gets and sets the expression used to calculate the value of the parameter. This is the equivalent of the "Expression" column in the Parameters dialog. Numeric parameters can be defined by a simple expression like "6.25", which will be interpreted based on whatever the default units are for the document. For example, if the units are set to millimeters, the value will be 6.25 mm; if the units are inches, it will be 6.25 inches. The expression can also contain the units so "6.25 in" will always be evaluated as inches regardless of the document units. |
| [id](CustomFeatureParameter_id.htm) | Returns the ID of this custom feature parameter. |
| [isDeletable](CustomFeatureParameter_isDeletable.htm) | Gets if this parameter can be deleted. Parameters that have dependents cannot be deleted, and model parameters typically cannot be deleted. However, there is the possibility in uncommon workflows where a model parameter no longer has any dependents, and it was not automatically deleted. In this case, this property will return true, and the deleteMe method can delete the parameter. |
| [isFavorite](CustomFeatureParameter_isFavorite.htm) | Gets and sets whether this parameter is included in the Favorites list in the parameters dialog |
| [isValid](CustomFeatureParameter_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVisible](CustomFeatureParameter_isVisible.htm) | Gets and sets if this parameter is visible in the parameters dialog. By default, all new parameters are visible.   This can be useful in cases where the feature can be edited to be in different states where a parameter is only valid in a certain state. You can change the visibility based on the current state of the feature and if that parameter should be available for edit. This implies that you create all the parameters that might be needed and then change their visibility based on the current state of the feature. The parameters that are not visible will not be returned by the ModelParameters collection and are only available through the custom feature they're associated with. |
| [modelParameters](CustomFeatureParameter_modelParameters.htm) | Returns the Collection containing the ModelParameter. |
| [name](CustomFeatureParameter_name.htm) | Gets and sets the name of the parameter. Setting the name can fail if the name is not unique with respect to all other parameters in the design. |
| [objectType](CustomFeatureParameter_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentCustomFeature](CustomFeatureParameter_parentCustomFeature.htm) | Returns the custom feature this parameter is associated with. |
| [role](CustomFeatureParameter_role.htm) | This property identifies what the parameter is used for. For an extrude, it could be "Depth", for a work plane it could be "Offset". |
| [textValue](CustomFeatureParameter_textValue.htm) | ![Preview](../images/TestTubeSmall.png)Gets and sets the value of the parameter when it is a text parameter. This can be determined by checking the valueType property. Setting this value will cause the current expression to be overwritten. If the parameter is not a text parameter, the value of this property should be ignored and setting will fail. |
| [unit](CustomFeatureParameter_unit.htm) | The unit type associated with this parameter. An empty string is returned for parameters that don't have a unit type. |
| [value](CustomFeatureParameter_value.htm) | Gets and sets the real value (a double) of the parameter in database units. Setting this property will set/reset the expression value for this parameter.   This property is only valid for numeric parameters and will fail for text parameters. You can determine the value type of the parameter by using the valueType property. Use the textValue property to get and set the value of text parameters. |
| [valueType](CustomFeatureParameter_valueType.htm) | ![Preview](../images/TestTubeSmall.png)Returns the type of value this parameter is. For a numeric parameter, you can get the value using the value property. For a text parameter, you can get the value using the textValue property. |

## Accessed From

[CustomFeatureParameters.item](CustomFeatureParameters_item.htm), [CustomFeatureParameters.itemById](CustomFeatureParameters_itemById.htm)

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |