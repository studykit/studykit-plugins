# StringProperty Object

Derived from: [Property](Property.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/StringProperty.h>

## Description

A string value property.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](StringProperty_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [id](StringProperty_id.htm) | Returns the unique ID of this property. |
| [isReadOnly](StringProperty_isReadOnly.htm) | Indicates if this property is read-only. If True any attempted edits will fail. |
| [isValid](StringProperty_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](StringProperty_name.htm) | Returns the name of this property as seen in the user interface. This name is localized and can change based on the current language |
| [objectType](StringProperty_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parent](StringProperty_parent.htm) | Returns the parent of this property.For properties associated with an appearance this will return the parent Appearance. For properties associated with a material, this will return the parent Material. For other types of properties, this will return the PropertyGroup it is in. |
| [value](StringProperty_value.htm) | Gets and sets the property value. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Library Item API Sample](LibraryItemSample_Sample.htm) | Demonstrates how to examine library items using the API.  To use the sample, create a new Python or C++ script and copy and paste this code, replacing the existing default code. The script will search for and record all components and library items in the current project. They are displayed in a dialog when the script has finished. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |