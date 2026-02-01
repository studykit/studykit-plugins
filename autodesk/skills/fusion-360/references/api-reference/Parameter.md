# Parameter Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Parameter.h>

## Description

The base class Parameter object that can represent model or user parameters.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](Parameter_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [attributes](Parameter_attributes.htm) | Returns the collection of attributes associated with this face. |
| [comment](Parameter_comment.htm) | The comment associated with this parameter |
| [dependencyParameters](Parameter_dependencyParameters.htm) | Returns a list of parameters that this parameter is dependent on. |
| [dependentParameters](Parameter_dependentParameters.htm) | Returns a list of parameters that are dependent on this parameter as a result of this parameter being referenced in their equation. |
| [entityToken](Parameter_entityToken.htm) | Returns a token for the Parameter object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same parameter. |
| [expression](Parameter_expression.htm) | Gets and sets the expression used to calculate the value of the parameter. This is the equivalent of the "Expression" column in the Parameters dialog. Numeric parameters can be defined by a simple expression like "6.25", which will be interpreted based on whatever the default units are for the document. For example, if the units are set to millimeters, the value will be 6.25 mm; if the units are inches, it will be 6.25 inches. The expression can also contain the units so "6.25 in" will always be evaluated as inches regardless of the document units.   An expression can also contain references to other parameters and use equations. For example, the expression "Length / 2" is valid for a numeric parameter as long as there is a numeric parameter named "Length". Expressions can also be used for text parameters, such as concatenating two other text parameters. For example, if there are two existing text parameters named text1 and text2, the expression for another text parameter can be "text1 + text2". More complex equations can also be used with text parameters like "if (Length < 20 mm; 'Short'; 'Long')" where "Length" is a numeric parameter. The resulting string can be obtained using the textValue property. |
| [isDeletable](Parameter_isDeletable.htm) | Gets if this parameter can be deleted. Parameters that have dependents cannot be deleted, and model parameters typically cannot be deleted. However, there is the possibility in uncommon workflows where a model parameter no longer has any dependents, and it was not automatically deleted. In this case, this property will return true, and the deleteMe method can delete the parameter. |
| [isFavorite](Parameter_isFavorite.htm) | Gets and sets whether this parameter is included in the Favorites list in the parameters dialog |
| [isValid](Parameter_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](Parameter_name.htm) | Gets and sets the name of the parameter. Setting the name can fail if the name is not unique with respect to all other parameters in the design. |
| [objectType](Parameter_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [textValue](Parameter_textValue.htm) | ![Preview](../images/TestTubeSmall.png)Gets and sets the value of the parameter when it is a text parameter. This can be determined by checking the valueType property. Setting this value will cause the current expression to be overwritten. If the parameter is not a text parameter, the value of this property should be ignored and setting will fail. |
| [unit](Parameter_unit.htm) | The unit type associated with this parameter. An empty string is returned for parameters that don't have a unit type. |
| [value](Parameter_value.htm) | Gets and sets the real value (a double) of the parameter in database units. Setting this property will set/reset the expression value for this parameter.   This property is only valid for numeric parameters and will fail for text parameters. You can determine the value type of the parameter by using the valueType property. Use the textValue property to get and set the value of text parameters. |
| [valueType](Parameter_valueType.htm) | ![Preview](../images/TestTubeSmall.png)Returns the type of value this parameter is. For a numeric parameter, you can get the value using the value property. For a text parameter, you can get the value using the textValue property. |

## Accessed From

[ConfigurationParameterColumn.parameter](ConfigurationParameterColumn_parameter.htm), [ConstructionPlaneAtAngleDefinition.angle](ConstructionPlaneAtAngleDefinition_angle.htm), [ConstructionPlaneDistanceOnPathDefinition.distance](ConstructionPlaneDistanceOnPathDefinition_distance.htm), [ConstructionPlaneOffsetDefinition.offset](ConstructionPlaneOffsetDefinition_offset.htm), [ConstructionPlaneTangentDefinition.angle](ConstructionPlaneTangentDefinition_angle.htm), [ParameterList.item](ParameterList_item.htm), [ParameterList.itemByName](ParameterList_itemByName.htm)

## Derived Classes

[ModelParameter](ModelParameter.htm), [UserParameter](UserParameter.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create Animation API Sample](CreateAnimation_Sample.htm) | Creates a series of images of a design where a parameter is being changed. The series of images can be used to create an animation using other software. To run this sample, have a part open that contains a parameter named "Length". The parameter should be able to be successfully modified from 10 to 15 centimeters. Run the sample and choose or create a directory for the output. After running you should have a folder full of images that are snapshots of each parameter value. |
| [Set parameters from a csv file and export to STEP](SetParametersFromACsvFileAndExportToSTEP_Sample.htm) | Reads data from a .csv file and sets user parameters in the model and then exports the model to STEP. When setting parameters be aware that this sample is setting user parameters. It's also possible to set model parameters but that's not demonstrated here. Also when accessing parameters, it is case sensitive so the names you use in your program much exactly match the names in the model. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |