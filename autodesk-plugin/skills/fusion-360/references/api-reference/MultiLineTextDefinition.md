# MultiLineTextDefinition Object

Derived from: [SketchTextDefinition](SketchTextDefinition.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/MultiLineTextDefinition.h>

## Description

Defines the information for multi-line text.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MultiLineTextDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [rotate](MultiLineTextDefinition_rotate.htm) | Rotates the text box. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [characterSpacing](MultiLineTextDefinition_characterSpacing.htm) | Gets and sets the spacing between the characters. This is an additional spacing to apply that is defined as a percentage of the default spacing. A spacing of 0 indicates no additional spacing. A spacing of 50 indicates to use the default plus 50% of the default. |
| [horizontalAlignment](MultiLineTextDefinition_horizontalAlignment.htm) | Gets and sets the horizontal alignment of the text with respect to the text rectangle. |
| [isValid](MultiLineTextDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](MultiLineTextDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentSketchText](MultiLineTextDefinition_parentSketchText.htm) | Returns the SketchText object this definition is associated with. This property will return null in the case the definition object was obtained from a SketchTextInput object because the SketchText object does not yet exist. |
| [rectangleLines](MultiLineTextDefinition_rectangleLines.htm) | Returns the four sketch lines that define the boundary of the sketch text. By adding constraints to these lines you can associatively control the size, position and angle of the sketch text. If the MultiLineTextDefinition object is obtained from a SketchTextInput object, this property will return null because the text and it's associated lines have not been created yet. |
| [verticalAlignment](MultiLineTextDefinition_verticalAlignment.htm) | Gets and sets the vertical alignment of the text with respect to the text rectangle. |

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |