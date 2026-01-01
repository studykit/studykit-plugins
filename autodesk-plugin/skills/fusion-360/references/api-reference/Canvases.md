# Canvases Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/Canvases.h>

## Description

Provides access to the Canvases in a component and provides the functionality to add new Canvases.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](Canvases_add.htm) | Creates a new canvas. Use the createInput method to first create an input object and set the available options. Then, pass that input object to the add method to create the canvas. |
| [classType](Canvases_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createInput](Canvases_createInput.htm) | Creates a new CanvasInput object. A CanvasInput object is the logical equivalent to the command dialog when creating a canvas. It provides access to the various options when creating a canvas. Calling the add method and passing in the CanvasInput is the equivalent to clicking the OK button on the dialog to create the canvas. |
| [item](Canvases_item.htm) | Returns the specified canvas using an index into the collection. |
| [itemByName](Canvases_itemByName.htm) | Returns the specified canvas using the name of the canvas. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](Canvases_count.htm) | Returns the number of canvases in the component. |
| [isValid](Canvases_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](Canvases_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[BaseComponent.canvases](BaseComponent_canvases.htm), [Component.canvases](Component_canvases.htm), [FlatPatternComponent.canvases](FlatPatternComponent_canvases.htm)

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |