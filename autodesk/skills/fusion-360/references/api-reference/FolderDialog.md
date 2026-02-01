# FolderDialog Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/FolderDialog.h>

## Description

Provides access to a folder selection dialog to allow the user to select a folder.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](FolderDialog_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [showDialog](FolderDialog_showDialog.htm) | Displays a modal dialog allowing the user to select a folder. The return value can be used to determine if the dialog was canceled without selecting a folder. the folder property can be used to get the selected folder. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [folder](FolderDialog_folder.htm) | Gets the folder selected by the user in the dialog. This property is used after the ShowDialog method has been called to retrieve the folder specified by the user. |
| [initialDirectory](FolderDialog_initialDirectory.htm) | Gets or sets the initial directory displayed by the file dialog box. |
| [isValid](FolderDialog_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](FolderDialog_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [title](FolderDialog_title.htm) | Gets or sets the title displayed on the dialog. |

## Accessed From

[UserInterface.createFolderDialog](UserInterface_createFolderDialog.htm)

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |