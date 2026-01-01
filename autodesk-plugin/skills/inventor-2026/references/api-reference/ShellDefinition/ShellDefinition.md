# ShellDefinition Object

## Description

## New Features of Inventor 2026

1. Updated the step #11 for Port to .Net 8 process (C# and VB.net projects)
   in article [Port .Net Framework-based project to .Net](PortToNetCore_Overview.md) to embed manifest with a simpler way.
2. New DrawingViewAnnotation object that allows to access the drawing view annotation information for detail and section drawing view.

   ![DrawingViewAnnotation](../images/DrawingViewAnnotation.png)
3. Hide Sketch3dOptions object, move the Sketch3dOptions.AutoBendWithLineCreation to SketchOptions, and exposed SketchOptions.SketchOpacity property.

   ![SketchOptions](../images/SketchOptions.png)
4. New SimplifyFeature object allows to create, edit and delete the simplify features in part documents.

   ![SimplifyFeature](../images/SimplifyFeature.png)
5. ContourFlangeDefinition is enhanced to make use of edge sets to set the extent, some functions are hidden to keep legacy behavior and new functions are exposed for the enhancement.

   ![ContourFlangeEdgeSet](../images/ContourFlangeEdgeSet.png)
6. New ShellFeatures.CreateDefinition method to replace ShellFeatures.CreateShellDefinition method to enhance the ShellDefinition with AffectedBodies and Method functions.

   ![ShellDefinition](../images/ShellDefinition.png)
7. New BreakOperation.AddBySketch function allows to create a break operation using an existing drawing sketch. And new BreakOperation.BreakLineSketch property can be used to return the drawing sketch that is used to create the break operation.

   ![BreakOperationOnSketch](../images/BreakOperationOnSketch.png)
8. New ClientFeature.ClientGraphicsVisible property allows to get and set the visibility of client graphics in a client feature.
9. Public the ComponentOccurrence.ActiveDesignViewRepresentation property.
10. Public the CosmeticWelds.Add and CreateDefinition methods.
11. New DrawingView.ShowTrails property allows to show or hide the trails for a drawing view of a presentation.

    ![ShowTrails](../images/ShowTrails.png)
12. New DimensionStyle.ExtendBeyondTicks property allows to set the extend distance beyond ticks. New DimensionStyle.ExtensionLine property allows to set the extention line distance. New DimensionStyle.UseCapitalXForEquallySpacedFeatures property allows to set whether to use captical X in equally spaced features or not.

    ![DimensionStyle2026](../images/DimensionStyle2026.png)
13. New DrawingStandardStyle.GetAvailableStyles and SetAvailableStyles allow to get and set the available styles.

    ![AvailableStyles](../images/AvailableStyles.png)
14. New DrawingStandardStyle.GetViewAnnotationDefaults and SetViewAnnotationDefaults functions allow to get and set the view annotation defaults for detail and section view.

    ![ViewAnnotationDefaults](../images/ViewAnnotationDefaults.png)
15. New FileDialogEvents.OnOptionsReset event allows to notify you when the options requires to be reset(e.g. when change the file types).
16. New FileManager.GetRevitFileVersionCreated method returns the Revit file version when it was created.
17. New ModelStates.ModelStatesInEdit property allows to get and set the model states that are in edit mode, and the MemberEditScope will return kEditMultipleMembers in this case.

    ![ModelStatesInEdit](../images/ModelStatesInEdit.png)
18. New Parameters.ExportToXML and ImportFromXML methods allow to import and export parameters.

    ![ParameterImportExport](../images/ParameterImportExport.png)
19. New RevitExportDefinition.RevitTemplate property allows to set the template when export to Revit.

    ![RevitTemplate](../images/RevitTemplate.png)
20. Change ContourFlangeFeature.Definition and PunchToolFeature.iFeatureDefinition properties as read-write properties so a definition object can be assigned to them to make multple changes with one recomputation.
21. Support new version type(IFC4x3) when export to IFC file using BIMComponet.ExportBuildingComponentWithOptions.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddThicknessFaceSet](../ShellDefinition/ShellDefinition_AddThicknessFaceSet.md) | Method that creates a new thickness face set. The new ShellThicknessFaceSet is returned. |
| [Copy](../ShellDefinition/ShellDefinition_Copy.md) | Method that returns a copy of the ShellDefinition object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AffectedBodies](../ShellDefinition/ShellDefinition_AffectedBodies.md) | Read-write property that specifies the solid bodies to be hollowed out. |
| [Application](../ShellDefinition/ShellDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ApproximationOptimized](../ShellDefinition/ShellDefinition_ApproximationOptimized.md) | Gets and sets whether the approximation is optimized. |
| [ApproximationTolerance](../ShellDefinition/ShellDefinition_ApproximationTolerance.md) | Gets and sets the approximation tolerance. |
| [ApproximationType](../ShellDefinition/ShellDefinition_ApproximationType.md) | Gets and sets the approximation method used for the feature. |
| [Direction](../ShellDefinition/ShellDefinition_Direction.md) | Gets and sets the shell boundary relative to part face. |
| [FaceSetCount](../ShellDefinition/ShellDefinition_FaceSetCount.md) | Property that specifies the number of face sets currently defined in the defintion. |
| [FaceSetItem](../ShellDefinition/ShellDefinition_FaceSetItem.md) | Method that returns the specified ShellThicknessFaceSet object from the collection. |
| [InputFaces](../ShellDefinition/ShellDefinition_InputFaces.md) | Gets and sets the faces that were specified to create or edit the Shell feature. |
| [Method](../ShellDefinition/ShellDefinition_Method.md) | Read-write property that gets and sets the shell method. This defaults to kSharpShellMethod when the definition is just created. |
| [Parent](../ShellDefinition/ShellDefinition_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [Thickness](../ShellDefinition/ShellDefinition_Thickness.md) | Property that returns the parameter that controls the thickness of the shell. This property will return Nothing if the shell feature has not been created yet. |
| [Type](../ShellDefinition/ShellDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ShellDefinition.Copy](../ShellDefinition/ShellDefinition_Copy.md), [ShellFeature.Definition](../ShellFeature/ShellFeature_Definition.md), [ShellFeatureProxy.Definition](../ShellFeatureProxy/ShellFeatureProxy_Definition.md), [ShellFeatures.CreateDefinition](../ShellFeatures/ShellFeatures_CreateDefinition.md)

## Version

Introduced in version 9
