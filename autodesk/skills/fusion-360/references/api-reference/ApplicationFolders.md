# ApplicationFolders Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/ApplicationFolders.h>

## Description

The ApplicationFolders object provides access to the paths of various folders associated with Fusion.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ApplicationFolders_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [appLogFilePath](ApplicationFolders_appLogFilePath.htm) | Returns the full filename for the current application log file. |
| [appStoreInstallPath](ApplicationFolders_appStoreInstallPath.htm) | Returns the path where apps from the Autodesk App Store are installed. |
| [defaultPathForScriptsAndAddIns](ApplicationFolders_defaultPathForScriptsAndAddIns.htm) | Gets and sets the default path for scripts and add-ins. This is the same as the defaultPathForScriptsAndAddIns property on the APIPreferences object. |
| [isValid](ApplicationFolders_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [materialsPath](ApplicationFolders_materialsPath.htm) | Returns the path where user-created material and appearance libraries are saved. |
| [objectType](ApplicationFolders_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [optionsPath](ApplicationFolders_optionsPath.htm) | Returns the path to the user-specific folder where Fusion saves various options. |
| [rootPath](ApplicationFolders_rootPath.htm) | Returns the path to the version-specific folder where Fusion is installed. |
| [userDataPath](ApplicationFolders_userDataPath.htm) | Returns the path where some user-specific data is stored. |

## Accessed From

[Application.applicationFolders](Application_applicationFolders.htm)

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |