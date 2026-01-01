# MultiAxisDPMFeedrateSettings Object ![Preview](../images/TestTubeLarge.png)

Derived from: [MultiAxisFeedrateSettings](MultiAxisFeedrateSettings.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MultiAxisDPMFeedrateSettings.h>

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

## Description

Specialization of MultiAxisFeedrateSettings for standard degrees per minute feedrates.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MultiAxisDPMFeedrateSettings_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [dpmType](MultiAxisDPMFeedrateSettings_dpmType.htm) | The DPM settings type |
| [feedMode](MultiAxisDPMFeedrateSettings_feedMode.htm) | The feedmode to use for the multi axis. |
| [isValid](MultiAxisDPMFeedrateSettings_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [maximumFeedrate](MultiAxisDPMFeedrateSettings_maximumFeedrate.htm) | The maximum feedrate value that can be output. |
| [objectType](MultiAxisDPMFeedrateSettings_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [outputTolerance](MultiAxisDPMFeedrateSettings_outputTolerance.htm) | The tolerance for deciding whether to output a feedrate value or not. It helps to minimize the output of multi-axis feedrate numbers. If the feedrate value is within this tolerance of the previous feedrate value, then it is set to the previous value. Value is in deg/min. |

## Derived Classes

[MultiAxisCombinationDPMFeedrateSettings](MultiAxisCombinationDPMFeedrateSettings.htm)

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |