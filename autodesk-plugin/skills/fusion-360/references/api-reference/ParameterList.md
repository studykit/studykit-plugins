# ParameterList Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ParameterList.h>

## Description

Transient object used to pass a set of parameters.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](ParameterList_add.htm) | Adds a parameter to the list. This does not create a new parameter, it adds an existing parameter to the list. Note that duplicates can exist in the list. |
| [classType](ParameterList_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [contains](ParameterList_contains.htm) | Indicates whether or not ParameterList collection contains a specified parameter |
| [create](ParameterList_create.htm) | Creates a parameter list that the client can use for various purposes. Use ParameterList.Add to add parameters to the list after creating it. |
| [find](ParameterList_find.htm) | Finds the specified parameter in the list. The search can be started at a specified index rather than from the beginning of the list. If not found, -1 is returned. |
| [item](ParameterList_item.htm) | Function that returns the specified parameter using an index into the collection. |
| [itemByName](ParameterList_itemByName.htm) | Returns the specified parameter using the name of the parameter as it is displayed in the parameters dialog |
| [removeByIndex](ParameterList_removeByIndex.htm) | Method that removes a parameter from the list using the index of the item in the list Will fail if the list is read only. |
| [removeByItem](ParameterList_removeByItem.htm) | Method that removes a parameter from the list by specifying the parameter (item) to remove |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](ParameterList_count.htm) | Returns the number of parameters in the collection. |
| [isReadOnly](ParameterList_isReadOnly.htm) | Indicates if the list is read-only Some lists returned by API calls (instead of lists created by the user) are read only. Items cannot be added or remove from such a list. |
| [isValid](ParameterList_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ParameterList_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[CustomFeatureParameter.dependencyParameters](CustomFeatureParameter_dependencyParameters.htm), [CustomFeatureParameter.dependentParameters](CustomFeatureParameter_dependentParameters.htm), [Design.allParameters](Design_allParameters.htm), [FlatPatternProduct.allParameters](FlatPatternProduct_allParameters.htm), [ModelParameter.dependencyParameters](ModelParameter_dependencyParameters.htm), [ModelParameter.dependentParameters](ModelParameter_dependentParameters.htm), [Parameter.dependencyParameters](Parameter_dependencyParameters.htm), [Parameter.dependentParameters](Parameter_dependentParameters.htm), [ParameterList.create](ParameterList_create.htm), [UserParameter.dependencyParameters](UserParameter_dependencyParameters.htm), [UserParameter.dependentParameters](UserParameter_dependentParameters.htm), [VariableRadiusFilletEdgeSet.midPositions](VariableRadiusFilletEdgeSet_midPositions.htm), [VariableRadiusFilletEdgeSet.midRadii](VariableRadiusFilletEdgeSet_midRadii.htm), [WorkingModel.allParameters](WorkingModel_allParameters.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create Animation API Sample](CreateAnimation_Sample.htm) | Creates a series of images of a design where a parameter is being changed. The series of images can be used to create an animation using other software. To run this sample, have a part open that contains a parameter named "Length". The parameter should be able to be successfully modified from 10 to 15 centimeters. Run the sample and choose or create a directory for the output. After running you should have a folder full of images that are snapshots of each parameter value. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |