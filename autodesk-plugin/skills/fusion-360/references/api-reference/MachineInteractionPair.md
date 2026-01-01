# MachineInteractionPair Object ![Preview](../images/TestTubeLarge.png)

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineInteractionPair.h>

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

## Description

MachineInteractionPair objects control how a pair of MachineItems interact with each other.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MachineInteractionPair_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [reset](MachineInteractionPair_reset.htm) | Clear this MachineInteractionPair. This pair will then represent two MachineItems that do not interact. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isCheckedForCollisions](MachineInteractionPair_isCheckedForCollisions.htm) | Whether these MachineItems should be checked for collisions. |
| [isIgnored](MachineInteractionPair_isIgnored.htm) | Whether this MachineInteractionPair will be ignored. |
| [isValid](MachineInteractionPair_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [item1](MachineInteractionPair_item1.htm) | The first MachineItem involved in this MachineInteractionPair. |
| [item2](MachineInteractionPair_item2.htm) | The second MachineItem involved in this MachineInteractionPair. |
| [objectType](MachineInteractionPair_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[InteractionsMachineElement.createMachineInteractionPair](InteractionsMachineElement_createMachineInteractionPair.htm), [InteractionsMachineElement.item](InteractionsMachineElement_item.htm)

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |