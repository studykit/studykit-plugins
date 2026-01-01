# MergeFacesFeatureInput Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MergeFacesFeatureInput.h>

## Description

This class defines the methods and properties that pertain to the definition of a merge face feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MergeFacesFeatureInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [creationOccurrence](MergeFacesFeatureInput_creationOccurrence.htm) | In order for geometry to be transformed correctly, an Occurrence for creation needs to be specified when the Merge is created based on geometry (e.g. faces) in another component AND (Merge) is not in the root component. The CreationOccurrence is analogous to the active occurrence in the UI |
| [inputFaces](MergeFacesFeatureInput_inputFaces.htm) | Gets and sets an array of BRepFace objects that define the faces the merge will be performed on. The faces need to be connected and from the same body (solid or surface). |
| [isChainSelection](MergeFacesFeatureInput_isChainSelection.htm) | Get and sets whether or not faces that are tangentially connected and from the same body (solid or surface) will be included in the faces to merge |
| [isValid](MergeFacesFeatureInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](MergeFacesFeatureInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[MergeFacesFeatures.createInput](MergeFacesFeatures_createInput.htm)

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |