# VolumetricSampler Object ![Preview](../images/TestTubeLarge.png)

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::volume" and the header file is <Volume/Volumetric/VolumetricSampler.h>

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

## Description

The VolumetricSampler object which is used for controled sampling of the volumetric model.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [addSamplePoints](VolumetricSampler_addSamplePoints.htm) | Appends sample points to the existing sample points to be used for sampling the volumetric model. |
| [classType](VolumetricSampler_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [clearSamplePoints](VolumetricSampler_clearSamplePoints.htm) | Clears the sample points that have been set for sampling the volumetric model. |
| [evaluate](VolumetricSampler_evaluate.htm) | Evaluates the volumetric model at the previously set sample points for the given node and returns the results. |
| [evaluateColor](VolumetricSampler_evaluateColor.htm) | Evaluates the color of the model at the previously set sample points and returns the results. |
| [evaluateDensity](VolumetricSampler_evaluateDensity.htm) | Evaluates the density of the model at the previously set sample points and returns the results. This value is what is used to determine the level set of the model. |
| [evaluateLevelSet](VolumetricSampler_evaluateLevelSet.htm) | Evaluates the level set function of the model at the previously set sample points and returns the results. |
| [samplePointCount](VolumetricSampler_samplePointCount.htm) | Gets the number of sample points that will be used for sampling the volumetric model. |
| [setBoundingBoxSampling](VolumetricSampler_setBoundingBoxSampling.htm) | Calculates and sets the sample points to be used for sampling the volumetric model for a given resolution throughout the bounding box provided. This will override any previously set sample points. |
| [setPlaneSampling](VolumetricSampler_setPlaneSampling.htm) | Calculates and sets the sample points to be used for sampling the volumetric model for a given resolution, plane and primary axis. The points will be distributed in a grid pattern on the plane, starting at the plane origin and extend in the primary axis and secodary axis for the axis size arguments. The secondary axis is calculated from the cross product of the plane normal and the primary axis. This will override any previously set sample points. |
| [setSamplePoints](VolumetricSampler_setSamplePoints.htm) | Sets sample points to be used for sampling the volumetric model. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](VolumetricSampler_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](VolumetricSampler_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[VolumetricModel.createSampler](VolumetricModel_createSampler.htm)

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |