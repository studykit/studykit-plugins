# CustomFeatureEvent Object ![Preview](../images/TestTubeLarge.png)

Derived from: [Event](Event.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CustomFeatureEvent.h>

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

## Description

A CustomFeature event is an event associated with handling changes to a custom feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](CustomFeatureEvent_add.htm) | Add a handler to be notified when the file event occurs. |
| [classType](CustomFeatureEvent_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [remove](CustomFeatureEvent_remove.htm) | Removes a handler from the event. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](CustomFeatureEvent_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](CustomFeatureEvent_name.htm) | The name of the event - e.g. "DocumentOpening" |
| [objectType](CustomFeatureEvent_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [sender](CustomFeatureEvent_sender.htm) | The object that is firing the event. For example, in the case of a command input event this will return the command. |

## Accessed From

[CustomFeatureDefinition.customFeatureCompute](CustomFeatureDefinition_customFeatureCompute.htm)

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |