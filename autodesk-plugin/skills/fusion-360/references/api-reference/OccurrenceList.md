# OccurrenceList Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/OccurrenceList.h>

## Description

Provides a list of occurrences.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](OccurrenceList_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](OccurrenceList_item.htm) | Returns the specified occurrence using an index into the collection. |
| [itemByName](OccurrenceList_itemByName.htm) | Returns the specified occurrence using the name of the occurrence. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](OccurrenceList_count.htm) | Returns the number of occurrences in the collection. |
| [isValid](OccurrenceList_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](OccurrenceList_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[BaseComponent.allOccurrences](BaseComponent_allOccurrences.htm), [BaseComponent.allOccurrencesByComponent](BaseComponent_allOccurrencesByComponent.htm), [BaseComponent.occurrencesByComponent](BaseComponent_occurrencesByComponent.htm), [Component.allOccurrences](Component_allOccurrences.htm), [Component.allOccurrencesByComponent](Component_allOccurrencesByComponent.htm), [Component.occurrencesByComponent](Component_occurrencesByComponent.htm), [FlatPatternComponent.allOccurrences](FlatPatternComponent_allOccurrences.htm), [FlatPatternComponent.allOccurrencesByComponent](FlatPatternComponent_allOccurrencesByComponent.htm), [FlatPatternComponent.occurrencesByComponent](FlatPatternComponent_occurrencesByComponent.htm), [Occurrence.childOccurrences](Occurrence_childOccurrences.htm), [Occurrences.asList](Occurrences_asList.htm), [RigidGroup.occurrences](RigidGroup_occurrences.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Assembly traversal using recursion API Sample](AssemblyTraversalUsingRecursion_Sample.htm) | Traverses the entire structure of the currently open assemlby using a recursive function and displays the result in a message box. This will match the occurrence structure seen in the browser. |
| [Create Setups From Hole Recognition API Sample](CreateSetupsFromHoleRecognition_Sample.htm) | This sample script demonstrates how to create a correctly oriented setup using Hole Recognition functionality.  The Fusion Manufacturing Extension is required for Hole Recognition.  The script starts by opening a sample model from the CAM Samples folder via its URN. The model comprises a 3 way coupling containing holes in various orientations and mounted on a fixture. A reference setup is created for the model using a simple stock mode and offsets. The Hole Recognition feature of the Fusion Manufacturing Extension creates 5 hole groups containing 11 holes between them. For each unique hole group vector captured, a new setup is created and its orientation transformed to match the vector. |
| [Get Volume of Active Design API Sample](GetsVolumeOfActiveDesign_Sample.htm) | Traverses through the active design and totals the volume of every body within the design. |
| [Set Vise Origin As Setup WCS Origin API Sample](SetViseOriginAsSetupWCSOrigin_Sample.htm) | This sample script demonstrates how to define our setup WCS origin relative to our vise origin from either a component, a sketch point or a joint origin.  The Work Coordinate System is a reference point set in our CAM workspace and on our machine. All machine coordinates are drawn from the WCS. This script demonstrates defining the WCS by each of 4 alternative methods:  Setup by default with no origin defined.  Setup using vise origin as WCS origin.  Setup using a sketch point as WCS origin.  Setup using a joint origin as WCS origin. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |