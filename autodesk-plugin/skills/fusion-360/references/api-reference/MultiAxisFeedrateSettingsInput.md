# MultiAxisFeedrateSettingsInput Object ![Preview](../images/TestTubeLarge.png)

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MultiAxisFeedrateSettingsInput.h>

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

## Description

Input class for creating MultiAxisFeedrateSettings objects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MultiAxisFeedrateSettingsInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [dpmType](MultiAxisFeedrateSettingsInput_dpmType.htm) | If the feedMode is MultiAxisFeedMode.MultiAxisFeedMode\_DegreesPerMinute, determines what type of MultiAxisCombinationDPMFeedrateSettings will create. |
| [feedMode](MultiAxisFeedrateSettingsInput_feedMode.htm) | The feed mode to use for the multi-axis feedrate settings. Determines the type of MultiAxisFeedrateSettings that will be created. |
| [isValid](MultiAxisFeedrateSettingsInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](MultiAxisFeedrateSettingsInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[MultiAxisMachineElement.createFeedrateSettingsInput](MultiAxisMachineElement_createFeedrateSettingsInput.htm)

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |