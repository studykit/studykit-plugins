# ControlDefinition Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ControlDefinition.h>

## Description

The ControlDefinition is the base class for the various types of control definitions. You can use properties on the control definition to define the look and behavior of the control.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ControlDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isEnabled](ControlDefinition_isEnabled.htm) | Gets or sets if this definition is enabled or not. This has the effect of enabling and disabling any associated controls. |
| [isValid](ControlDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVisible](ControlDefinition_isVisible.htm) | Gets or sets if this definition is visible or not. This has the effect of making any associated controls visible or invisible in the user interface. |
| [name](ControlDefinition_name.htm) | Gets or sets the name for this control. This is the visible name displayed in the user interface. |
| [objectType](ControlDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[CommandDefinition.controlDefinition](CommandDefinition_controlDefinition.htm)

## Derived Classes

[ButtonControlDefinition](ButtonControlDefinition.htm), [CheckBoxControlDefinition](CheckBoxControlDefinition.htm), [ListControlDefinition](ListControlDefinition.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |