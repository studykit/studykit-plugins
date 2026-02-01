# AlongPathTextDefinition Object

Derived from: [SketchTextDefinition](SketchTextDefinition.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/AlongPathTextDefinition.h>

## Description

Defines the information for text that follows along a path.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](AlongPathTextDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [characterSpacing](AlongPathTextDefinition_characterSpacing.htm) | Gets and sets the spacing between the characters. This is an additional spacing to apply that is defined as a percentage of the default spacing. A spacing of 0 indicates no additional spacing. A spacing of 50 indicates to use the default plus 50% of the default. |
| [horizontalAlignment](AlongPathTextDefinition_horizontalAlignment.htm) | Gets and sets the horizontal alignment of the text with respect to the path curve. |
| [isAbovePath](AlongPathTextDefinition_isAbovePath.htm) | Gets and sets if the text should be positioned above or below the path entity. |
| [isValid](AlongPathTextDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](AlongPathTextDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentSketchText](AlongPathTextDefinition_parentSketchText.htm) | Returns the SketchText object this definition is associated with. This property will return null in the case the definition object was obtained from a SketchTextInput object because the SketchText object does not yet exist. |
| [path](AlongPathTextDefinition_path.htm) | Get and sets the entity that defines the path for the text. This can be a SketchCurve or BRepEdge object. |

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |