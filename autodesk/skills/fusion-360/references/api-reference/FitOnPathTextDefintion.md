# FitOnPathTextDefintion Object

Derived from: [SketchTextDefinition](SketchTextDefinition.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/FitOnPathTextDefintion.h>

## Description

Defines the information for text that fits along a path.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](FitOnPathTextDefintion_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isAbovePath](FitOnPathTextDefintion_isAbovePath.htm) | Gets and sets if the text should be positioned above or below the path entity. |
| [isValid](FitOnPathTextDefintion_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](FitOnPathTextDefintion_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentSketchText](FitOnPathTextDefintion_parentSketchText.htm) | Returns the SketchText object this definition is associated with. This property will return null in the case the definition object was obtained from a SketchTextInput object because the SketchText object does not yet exist. |
| [path](FitOnPathTextDefintion_path.htm) | Get and sets the entity that defines the path for the text. This can be a SketchCurve or BRepEdge object. |

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |