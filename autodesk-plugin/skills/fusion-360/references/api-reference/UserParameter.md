# UserParameter Object

Derived from: [Parameter](Parameter.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/UserParameter.h>

## Description

Represents a User Parameter.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](UserParameter_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteMe](UserParameter_deleteMe.htm) | Deletes the user parameter A parameter can only be deleted if it is a UserParameter and it is not referenced by other parameters. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [attributes](UserParameter_attributes.htm) | Returns the collection of attributes associated with this face. |
| [comment](UserParameter_comment.htm) | The comment associated with this parameter |
| [dependencyParameters](UserParameter_dependencyParameters.htm) | Returns a list of parameters that this parameter is dependent on. |
| [dependentParameters](UserParameter_dependentParameters.htm) | Returns a list of parameters that are dependent on this parameter as a result of this parameter being referenced in their equation. |
| [design](UserParameter_design.htm) | Returns the Design containing the UserParameter. |
| [entityToken](UserParameter_entityToken.htm) | Returns a token for the Parameter object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same parameter. |
| [expression](UserParameter_expression.htm) | Gets and sets the expression used to calculate the value of the parameter. This is the equivalent of the "Expression" column in the Parameters dialog. Numeric parameters can be defined by a simple expression like "6.25", which will be interpreted based on whatever the default units are for the document. For example, if the units are set to millimeters, the value will be 6.25 mm; if the units are inches, it will be 6.25 inches. The expression can also contain the units so "6.25 in" will always be evaluated as inches regardless of the document units.   An expression can also contain references to other parameters and use equations. For example, the expression "Length / 2" is valid for a numeric parameter as long as there is a numeric parameter named "Length". Expressions can also be used for text parameters, such as concatenating two other text parameters. For example, if there are two existing text parameters named text1 and text2, the expression for another text parameter can be "text1 + text2". More complex equations can also be used with text parameters like "if (Length < 20 mm; 'Short'; 'Long')" where "Length" is a numeric parameter. The resulting string can be obtained using the textValue property. |
| [isDeletable](UserParameter_isDeletable.htm) | Gets if this parameter can be deleted. Parameters that have dependents cannot be deleted, and model parameters typically cannot be deleted. However, there is the possibility in uncommon workflows where a model parameter no longer has any dependents, and it was not automatically deleted. In this case, this property will return true, and the deleteMe method can delete the parameter. |
| [isFavorite](UserParameter_isFavorite.htm) | Gets and sets whether this parameter is included in the Favorites list in the parameters dialog |
| [isValid](UserParameter_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](UserParameter_name.htm) | Gets and sets the name of the parameter. Setting the name can fail if the name is not unique with respect to all other parameters in the design. |
| [objectType](UserParameter_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [textValue](UserParameter_textValue.htm) | ![Preview](../images/TestTubeSmall.png)Gets and sets the value of the parameter when it is a text parameter. This can be determined by checking the valueType property. Setting this value will cause the current expression to be overwritten. If the parameter is not a text parameter, the value of this property should be ignored and setting will fail. |
| [unit](UserParameter_unit.htm) | The unit type associated with this parameter. An empty string is returned for parameters that don't have a unit type. |
| [userParameters](UserParameter_userParameters.htm) | Returns the Collection containing the UserParameter. |
| [value](UserParameter_value.htm) | Gets and sets the real value (a double) of the parameter in database units. Setting this property will set/reset the expression value for this parameter.   This property is only valid for numeric parameters and will fail for text parameters. You can determine the value type of the parameter by using the valueType property. Use the textValue property to get and set the value of text parameters. |
| [valueType](UserParameter_valueType.htm) | ![Preview](../images/TestTubeSmall.png)Returns the type of value this parameter is. For a numeric parameter, you can get the value using the value property. For a text parameter, you can get the value using the textValue property. |

## Accessed From

[UserParameters.add](UserParameters_add.htm), [UserParameters.asArray](UserParameters_asArray.htm), [UserParameters.item](UserParameters_item.htm), [UserParameters.itemByName](UserParameters_itemByName.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |