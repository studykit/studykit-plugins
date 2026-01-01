# Features Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

The features collection which provides access to all existing features. This collection provides direct access to all features regardless of type. It also provides access to type specific collections where you can get features of a specific type and also create new features of that type.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](Features_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createPath](Features_createPath.htm) | Method that creates a Path used to define the shape of a Sweep feature. A Path is a contiguous set of curves that can be a combination of sketch curves and model edges. |
| [item](Features_item.htm) | Function that returns the specified feature using an index into the collection. |
| [itemByName](Features_itemByName.htm) | Function that returns the specified feature using the name of the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [arrangeFeatures](Features_arrangeFeatures.htm) | ![Preview](../images/TestTubeSmall.png)Returns the collection that provides access to the Arrange features within the component and supports the creation of new Arrange features. |
| [baseFeatures](Features_baseFeatures.htm) | Returns the collection that provides access to the existing base features and supports the creation of new base features. A base feature represents a body that is non-parametric. |
| [bossFeatures](Features_bossFeatures.htm) | Returns the collection that provides access to the boss features within the component and supports the creation of new boss features. |
| [boundaryFillFeatures](Features_boundaryFillFeatures.htm) | Returns the collection that provides access to the Boundary Fill features within the component and supports the creation of new Boundary Fill features. |
| [boxFeatures](Features_boxFeatures.htm) | Returns the collection that provides access to the existing box features. |
| [chamferFeatures](Features_chamferFeatures.htm) | Returns the collection that provides access to the chamfer features within the component and supports the creation of new chamfer features. |
| [circularPatternFeatures](Features_circularPatternFeatures.htm) | Returns the collection that provides access to the circular pattern features within the component and supports the creation of new circular pattern features. |
| [coilFeatures](Features_coilFeatures.htm) | Returns the collection that provides access to the Coil Primitive features within the component. |
| [combineFeatures](Features_combineFeatures.htm) | Returns the collection that provides access to the combine features within the component and supports the creation of new combine features. |
| [copyPasteBodies](Features_copyPasteBodies.htm) | Returns the collection that provides access to the existing copy-paste features and supports the creation of new copy-paste features. |
| [count](Features_count.htm) | Returns the number of features in the collection. |
| [customFeatures](Features_customFeatures.htm) | ![Preview](../images/TestTubeSmall.png)Returns the collection that provides access to the custom features within the component and supports the creation of new custom features. |
| [cutPasteBodies](Features_cutPasteBodies.htm) | Returns the collection that provides access to the existing cut-paste features and supports the creation of new cut-paste features. |
| [cylinderFeatures](Features_cylinderFeatures.htm) | Returns the collection that provides access to the existing cylinder features. |
| [deleteFaceFeatures](Features_deleteFaceFeatures.htm) | Returns the collection that provides access to the existing Delete Face features. |
| [draftFeatures](Features_draftFeatures.htm) | Returns the collection that provides access to the draft features within the component and supports the creation of new draft features. |
| [embossFeatures](Features_embossFeatures.htm) | ![Preview](../images/TestTubeSmall.png)Returns the collection that provides access to the emboss features within the component and supports the creation of new emboss features. |
| [extendFeatures](Features_extendFeatures.htm) | Returns the collection that provides access to the Extend features within the component and supports the creation of new Extend features. |
| [extrudeFeatures](Features_extrudeFeatures.htm) | Returns the collection that provides access to the extrude features within the component and supports the creation of new extrude features. |
| [filletFeatures](Features_filletFeatures.htm) | Returns the collection that provides access to the fillet features within the component and supports the creation of new fillet features. |
| [flangeFeatures](Features_flangeFeatures.htm) | Returns the collection that provides access to the existing flange features. |
| [formFeatures](Features_formFeatures.htm) | Returns the collection that provides access to the existing form features. |
| [hemFeatures](Features_hemFeatures.htm) | ![Preview](../images/TestTubeSmall.png)Returns the collection that provides access to the existing Hem features. |
| [holeFeatures](Features_holeFeatures.htm) | Returns the collection that provides access to the hole features within the component and supports the creation of new hole features. |
| [isValid](Features_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [loftFeatures](Features_loftFeatures.htm) | Returns the collection that provides access to the existing loft features and supports the creation of new loft features. |
| [mergeFacesFeatures](Features_mergeFacesFeatures.htm) | Returns the collection object that supports the ability to merge faces. Merging faces is currently limited to a Direct Modeling design or a body in a base feature. The result of merging faces is a direct B-Rep modification, and the change is not represented as a feature in the browser. |
| [meshCombineFaceGroupsFeatures](Features_meshCombineFaceGroupsFeatures.htm) | ![Preview](../images/TestTubeSmall.png)Returns the collection that provides access to the mesh combine face groups features within the component and supports the creation of new mesh combine face groups features. |
| [meshCombineFeatures](Features_meshCombineFeatures.htm) | ![Preview](../images/TestTubeSmall.png)Returns the collection that provides access to the mesh combine features within the component and supports the creation of new mesh combine features. |
| [meshConvertFeatures](Features_meshConvertFeatures.htm) | ![Preview](../images/TestTubeSmall.png)Returns the collection that provides access to the mesh convert features within the component and supports the creation of new mesh convert features. |
| [meshGenerateFaceGroupsFeatures](Features_meshGenerateFaceGroupsFeatures.htm) | ![Preview](../images/TestTubeSmall.png)Returns the collection that provides access to the mesh generate facegroup features within the component and supports the creation of new mesh generate facegroup features. |
| [meshReduceFeatures](Features_meshReduceFeatures.htm) | ![Preview](../images/TestTubeSmall.png)Returns the collection that provides access to the mesh reduce features within the component and supports the creation of new mesh reduce features. |
| [meshRemeshFeatures](Features_meshRemeshFeatures.htm) | ![Preview](../images/TestTubeSmall.png)Returns the collection that provides access to the mesh remesh features within the component and supports the creation of new mesh remesh features. |
| [meshRepairFeatures](Features_meshRepairFeatures.htm) | ![Preview](../images/TestTubeSmall.png)Returns the collection that provides access to the mesh repair features within the component and supports the creation of new mesh repair features. |
| [meshReverseNormalFeatures](Features_meshReverseNormalFeatures.htm) | ![Preview](../images/TestTubeSmall.png)Returns the collection that provides access to the mesh reverse normal features within the component and supports the creation of new mesh reverse normal features. |
| [meshSeparateFeatures](Features_meshSeparateFeatures.htm) | ![Preview](../images/TestTubeSmall.png)Returns the collection that provides access to the mesh separate features within the component and supports the creation of new mesh separate features. |
| [meshShellFeatures](Features_meshShellFeatures.htm) | ![Preview](../images/TestTubeSmall.png)Returns the collection that provides access to the mesh shell features within the component and supports the creation of new mesh shell features. |
| [meshSmoothFeatures](Features_meshSmoothFeatures.htm) | ![Preview](../images/TestTubeSmall.png)Returns the collection that provides access to the mesh smooth features within the component and supports the creation of new mesh smooth features. |
| [mirrorFeatures](Features_mirrorFeatures.htm) | Returns the collection that provides access to the mirror features within the component and supports the creation of new mirror features. |
| [moveFeatures](Features_moveFeatures.htm) | Returns the collection that provides access to the Move features within the component and supports the creation of new Move features. |
| [objectType](Features_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [offsetFacesFeatures](Features_offsetFacesFeatures.htm) | Returns the collection that provides access to the existing Offset Face features. |
| [offsetFeatures](Features_offsetFeatures.htm) | Returns the collection that provides access to the Offset features within the component and supports the creation of new Offset features. |
| [patchFeatures](Features_patchFeatures.htm) | Returns the collection that provides access to the Patch features within the component and supports the creation of new Patch features. |
| [pathPatternFeatures](Features_pathPatternFeatures.htm) | Returns the collection that provides access to the path pattern features within the component and supports the creation of new path pattern features. |
| [pipeFeatures](Features_pipeFeatures.htm) | Returns the collection that provides access to the existing pipe features. |
| [rectangularPatternFeatures](Features_rectangularPatternFeatures.htm) | Returns the collection that provides access to the rectangular pattern features within the component and supports the creation of new rectangular pattern features. |
| [refoldFeatures](Features_refoldFeatures.htm) | Returns the collection that provides access to the existing refold features. |
| [removeFeatures](Features_removeFeatures.htm) | Returns the collection that provides access to the Remove features within the component and supports the creation of new Remove features. |
| [replaceFaceFeatures](Features_replaceFaceFeatures.htm) | Returns the collection that provides access to the replaceFace features within the component and supports the creation of new replaceFace features. |
| [reverseNormalFeatures](Features_reverseNormalFeatures.htm) | Returns the collection that provides access to the Reverse Normal features within the component and supports the creation of new Reverse Normal features. |
| [revolveFeatures](Features_revolveFeatures.htm) | Returns the collection that provides access to the revolve features within the component and supports the creation of new revolved features. |
| [ribFeatures](Features_ribFeatures.htm) | Returns the collection that provides access to the existing rib features. |
| [ripFeatures](Features_ripFeatures.htm) | Returns the collection that provides access to the existing Rip features. |
| [ruledSurfaceFeatures](Features_ruledSurfaceFeatures.htm) | Returns the collection that provides access to the Ruled Surface features within the component and supports the creation of new Ruled Surface features. |
| [ruleFilletFeatures](Features_ruleFilletFeatures.htm) | Returns the collection that provides access to the existing form features. |
| [scaleFeatures](Features_scaleFeatures.htm) | Returns the collection that provides access to the scale features within the component and supports the creation of new scale features. |
| [shellFeatures](Features_shellFeatures.htm) | Returns the collection that provides access to the shell features within the component and supports the creation of new shell features. |
| [silhouetteSplitFeatures](Features_silhouetteSplitFeatures.htm) | Returns the collection that provides access to the Parting Line Split features within the component and supports the creation of new Parting Line Split features |
| [sphereFeatures](Features_sphereFeatures.htm) | Returns the collection that provides access to the existing sphere features. |
| [splitBodyFeatures](Features_splitBodyFeatures.htm) | Returns the collection that provides access to the SplitBody features within the component and supports the creation of new SplitBody features |
| [splitFaceFeatures](Features_splitFaceFeatures.htm) | Returns the collection that provides access to the SplitFace features within the component and supports the creation of new SplitFace features |
| [stitchFeatures](Features_stitchFeatures.htm) | Returns the collection that provides access to the Stitch features within the component and supports the creation of new Stitch features. |
| [surfaceDeleteFaceFeatures](Features_surfaceDeleteFaceFeatures.htm) | Returns the collection that provides access to the existing Surface Delete Face features. |
| [sweepFeatures](Features_sweepFeatures.htm) | Returns the collection that provides access to the sweep features within the component and supports the creation of new sweep features. |
| [tessellateFeatures](Features_tessellateFeatures.htm) | ![Preview](../images/TestTubeSmall.png)Returns the collection that provides access to the tessellate features within the component and supports the creation of new tessellate features. |
| [thickenFeatures](Features_thickenFeatures.htm) | Returns the collection that provides access to the Thicken features within the component and supports the creation of new Thicken features. |
| [threadFeatures](Features_threadFeatures.htm) | Returns the collection that provides access to the thread features within the component and supports the creation of new thread features. |
| [torusFeatures](Features_torusFeatures.htm) | Returns the collection that provides access to the existing torus features. |
| [trimFeatures](Features_trimFeatures.htm) | Returns the collection that provides access to the Trim features within the component and supports the creation of new Trim features. |
| [unfoldFeatures](Features_unfoldFeatures.htm) | Returns the collection that provides access to the existing unfold features. |
| [unstitchFeatures](Features_unstitchFeatures.htm) | Returns the collection that provides access to the Unstitch features within the component and supports the creation of new Unstitch features. |
| [untrimFeatures](Features_untrimFeatures.htm) | Returns the collection that provides access to the Untrim features within the component and supports the creation of new Untrim features. |
| [volumetricCustomFeatures](Features_volumetricCustomFeatures.htm) | ![Preview](../images/TestTubeSmall.png)Returns the collection that provides access to volumetric custom features within the component and supports the creation of new volumetric custom features. |
| [volumetricModelToMeshFeatures](Features_volumetricModelToMeshFeatures.htm) | ![Preview](../images/TestTubeSmall.png)Returns the collection that provides access to the Volumetric Model to Mesh features within the component and supports the creation of new Volumetric Model to Mesh features. |
| [webFeatures](Features_webFeatures.htm) | Returns the collection that provides access to the existing web features. |

## Accessed From

[Component.features](Component_features.htm), [FlatPatternComponent.features](FlatPatternComponent_features.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Loft Feature API Sample](LoftFeatureSample_Sample.htm) | Demonstrates creating a new loft feature. |
| [Patch Feature API Sample](PatchFeatureSample_Sample.htm) | Demonstrates creating a new patch feature. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |