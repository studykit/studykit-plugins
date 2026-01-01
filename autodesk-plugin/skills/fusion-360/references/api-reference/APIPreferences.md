# APIPreferences Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/APIPreferences.h>

## Description

Provides access to the various preferences associated with the API.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](APIPreferences_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [debuggingPort](APIPreferences_debuggingPort.htm) | Gets and sets the port used when connecting to Visual Studio Code. |
| [defaultAddInLanguage](APIPreferences_defaultAddInLanguage.htm) | Gets and sets the preference that controls which programming language should be used when creating a new add-in. One option is to prompt the user. |
| [defaultPathForScriptsAndAddIns](APIPreferences_defaultPathForScriptsAndAddIns.htm) | The default path where new scripts or add-ins will be created. Scripts will be created in a "Scripts" subdirectory and add-ins will be created in an "AddIns" subdirectory. This must be the full path to the parent folder. |
| [defaultScriptLanguage](APIPreferences_defaultScriptLanguage.htm) | Gets and sets the preference that controls which programming language should be used when creating a new script. One option is to prompt the user. |
| [isDeveloperToolsEnabled](APIPreferences_isDeveloperToolsEnabled.htm) | Gets and sets if access to "Developer Tools" should be enabled in pallets and BrowserCommandInputs. |
| [isValid](APIPreferences_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](APIPreferences_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |

## Accessed From

[Preferences.apiPreferences](Preferences_apiPreferences.htm)

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |