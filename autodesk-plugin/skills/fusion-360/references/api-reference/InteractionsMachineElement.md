# InteractionsMachineElement Object ![Preview](../images/TestTubeLarge.png)

Derived from: [MachineElement](MachineElement.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/InteractionsMachineElement.h>

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

## Description

Machine element representing the machine's interactions. This controls how MachineItems interact with each other.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [apply](InteractionsMachineElement_apply.htm) | Add an MachineInteractionPair. This will overwrite any existing MachineInteractionPair with the same item1 and item2. |
| [classType](InteractionsMachineElement_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createMachineInteractionPair](InteractionsMachineElement_createMachineInteractionPair.htm) | Create a MachineInteractionPair that will control how the two items interact. |
| [createMachineItem](InteractionsMachineElement_createMachineItem.htm) | Create a MachineItem. |
| [item](InteractionsMachineElement_item.htm) | Get the MachineInteractionPair at index in this collection. |
| [resetMachineInteractionPairs](InteractionsMachineElement_resetMachineInteractionPairs.htm) | Restore all MachineInteractionPairs to their defaults. |
| [staticTypeId](InteractionsMachineElement_staticTypeId.htm) | Identifying name for all elements of this type. Pass this to the itemByType or itemById methods of MachineElements to filter to elements of this type. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](InteractionsMachineElement_count.htm) | Get the number of pairs in this collection. |
| [elementId](InteractionsMachineElement_elementId.htm) | Identifier for this element. Unique within an element type. |
| [isValid](InteractionsMachineElement_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](InteractionsMachineElement_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [typeId](InteractionsMachineElement_typeId.htm) | Identifier for this type of machine element. |

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |