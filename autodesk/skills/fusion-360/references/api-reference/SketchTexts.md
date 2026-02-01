# SketchTexts Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchTexts.h>

## Description

The collection of text blocks in a sketch. This provides access to the existing text blocks and supports creating new text blocks.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](SketchTexts_add.htm) | Creates a sketch text. |
| [classType](SketchTexts_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createInput](SketchTexts_createInput.htm) | \*\*RETIRED\*\* Creates a SketchTextInput object that can be used to define additional settings when creating sketch text. The SketchTextInput object is equivalent to the Sketch Text dialog in that it collects all of the input required to create sketch text. Once the properties of the SketchTextInput object have been defined, use the add method to create the sketch text. |
| [createInput2](SketchTexts_createInput2.htm) | Creates a SketchTextInput object that is used to define the additional input to create text. The SketchTextInput object is equivalent to the Sketch Text dialog in that it collects all of the input required to create sketch text. You must call setAsFitOnPath, setAsAlongPath, or setAsMultiLine methods to define one of the three types of text and can use other and define any setAs Once the properties of the SketchTextInput object have been defined, use the add method to create the sketch text. |
| [item](SketchTexts_item.htm) | Function that returns the specified sketch text using an index into the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](SketchTexts_count.htm) | Returns the number of texts in the sketch. |
| [isValid](SketchTexts_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](SketchTexts_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Sketch.sketchTexts](Sketch_sketchTexts.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SketchTextInput.setAsAlongPath](SketchTextinput_setAsAlongPath_Sample.htm) | Demonstrates the SketchTextInput.setAsAlongPath method. |
| [SketchTextInput.setAsFitOnPath](SketchTextInput_setAsFitOnPath_Sample.htm) | Demoonstrates the SketchTextInput.setAsFitOnPath method. |
| [SketchTextInput.setAsMultiLine](SketchTextInput_setAsMultiLine_Sample.htm) | Demonstrates the SketchTextInput.setAsMultiLine method. |
| [Sketch Text API Sample](SketchTextSample_Sample.htm) | Demonstrates creating sketch text by creating both mult-line text and text along a curve. |

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |