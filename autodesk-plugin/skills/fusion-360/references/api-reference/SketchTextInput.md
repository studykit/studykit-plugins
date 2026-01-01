# SketchTextInput Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchTextInput.h>

## Description

The SketchTextInput object is equivalent to the Sketch Text dialog in that it collects all of the input required to create sketch text. Once the properties of the SketchTextInput object have been defined, use the add method to create the sketch text. A SketchTextInput object is created by using the createInput of the SketchTexts object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](SketchTextInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [setAsAlongPath](SketchTextInput_setAsAlongPath.htm) | Sets this SketchTextInput to define text that follows along a specified path. |
| [setAsFitOnPath](SketchTextInput_setAsFitOnPath.htm) | Sets this SketchTextInput to define text that fits along a specified path. Fitting on a path will space the characters so the text fits along the entire length of the path entity. |
| [setAsMultiLine](SketchTextInput_setAsMultiLine.htm) | Defines the first corner point of the rectangle that will contain the text. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [angle](SketchTextInput_angle.htm) | \*\*RETIRED\*\* Gets and sets the angle of the text relative to the x-axis of the x-y plane of the sketch. |
| [definition](SketchTextInput_definition.htm) | Returns the SketchTextDefinition object associated with this input. When the SketchTextInput is first created this property will return null. Once one of the "set" methods have been called, this will return the SketchTextDefinition of the appropriate type and can be used to make any additional changes to the text. |
| [fontName](SketchTextInput_fontName.htm) | Gets and sets the name of the font to use. |
| [height](SketchTextInput_height.htm) | Gets and sets the height of the text in centimeters. |
| [isHorizontalFlip](SketchTextInput_isHorizontalFlip.htm) | Gets and sets if the text is flipped horizontally. |
| [isValid](SketchTextInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVerticalFlip](SketchTextInput_isVerticalFlip.htm) | Gets and sets if the text is flipped vertically. |
| [objectType](SketchTextInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [position](SketchTextInput_position.htm) | \*\*RETIRED\*\* Gets and sets the position of the text on the x-y plane of the sketch. The text must lie on the x-y plane so the Z component of the point is ignored and always treated as zero. |
| [text](SketchTextInput_text.htm) | Gets and sets the text. |
| [textStyle](SketchTextInput_textStyle.htm) | Gets and sets the text style to apply to the entire text. This is a bitwise enum so styles can be combined to apply multiple styles. For example you can apply bold and italic. |

## Accessed From

[SketchTexts.createInput](SketchTexts_createInput.htm), [SketchTexts.createInput2](SketchTexts_createInput2.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sketch Text API Sample](SketchTextSample_Sample.htm) | Demonstrates creating sketch text by creating both mult-line text and text along a curve. |

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |