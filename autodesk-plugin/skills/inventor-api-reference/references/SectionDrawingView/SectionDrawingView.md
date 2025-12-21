# SectionDrawingView Object

Derived from: [DrawingView](../DrawingView/DrawingView.md) Object

## Description

The SectionDrawingView object represents a section view within a drawing. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Align](../SectionDrawingView/SectionDrawingView_Align.md) | Method that aligns this view with the input drawing view. The method returns a failure if the view is already aligned. Use the Aligned property to check for this condition and to break existing alignment. |
| [AlignAuxiliary](../SectionDrawingView/SectionDrawingView_AlignAuxiliary.md) | Method that re-aligns an auxiliary view. The method fails if the view is not an auxiliary view. |
| [CopyTo](../SectionDrawingView/SectionDrawingView_CopyTo.md) | Method that copies this drawing view into the specified sheet. The new object is returned. |
| [CreateOriginIndicator](../SectionDrawingView/SectionDrawingView_CreateOriginIndicator.md) | Method that creates the origin indicator for ordinate dimensions and hole tables. The specified input GeometryIntent object must be associated with this drawing view, otherwise this method will fail. |
| [Delete](../SectionDrawingView/SectionDrawingView_Delete.md) | Method that deletes the DrawingView. |
| [DrawingViewToModelSpace](../SectionDrawingView/SectionDrawingView_DrawingViewToModelSpace.md) | Method that takes a 2d coordinate in drawing view space, and returns a Line in model space. Since this method transforms from 2D space to 3D space, there is insufficient information to obtain a 3D model point. Hence, this method returns a Line in the view direction on which the point lies. You may then use the FindUsingRay method to find the point(s) of interest. |
| [DrawingViewToSheetSpace](../SectionDrawingView/SectionDrawingView_DrawingViewToSheetSpace.md) | Method that takes a 2d coordinate in drawing view space, and returns a Point2d containing the coordinates of the point in sheet space. |
| [GetAutomatedCenterlineSettings](../SectionDrawingView/SectionDrawingView_GetAutomatedCenterlineSettings.md) | Method that returns the settings that define how automatic center lines and center marks are to be calculated for this view. |
| [GetComponentLineColor](../SectionDrawingView/SectionDrawingView_GetComponentLineColor.md) | Method that gets color of a component in drawing view. |
| [GetHiddenLinesStatus](../SectionDrawingView/SectionDrawingView_GetHiddenLinesStatus.md) | Method that gets the hidden lines status of a component in the drawing view. |
| [GetIncludeStatus](../SectionDrawingView/SectionDrawingView_GetIncludeStatus.md) | Method that gets the include status of the input object in the drawing view. |
| [GetReferenceKey](../SectionDrawingView/SectionDrawingView_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetVisibility](../SectionDrawingView/SectionDrawingView_GetVisibility.md) | Method that gets the visibility of the input object in the drawing view. This returns error if the input object has partial visibility status. |
| [GetWeldmentState](../SectionDrawingView/SectionDrawingView_GetWeldmentState.md) | Method that gets the weldment option for the drawing view. The method returns a failure if the referenced model does not contain weldments. |
| [InsertInModelSpace](../SectionDrawingView/SectionDrawingView_InsertInModelSpace.md) | Inserts the view geometry into model space only if the drawing lives in an Inventor DWG file. |
| [ModelToDrawingViewSpace](../SectionDrawingView/SectionDrawingView_ModelToDrawingViewSpace.md) | Method that takes a 3d coordinate in model space, and returns a Point2d object containing the coordinate point in drawing view space. |
| [ModelToSheetSpace](../SectionDrawingView/SectionDrawingView_ModelToSheetSpace.md) | Method that takes a 3d coordinate in model space, and returns a Point2d object containing the coordinate point in sheet space. |
| [MoveTo](../SectionDrawingView/SectionDrawingView_MoveTo.md) | Method that moves this drawing view into the specified sheet. The moved object is returned. |
| [ReverseDirection](../SectionDrawingView/SectionDrawingView_ReverseDirection.md) | Method that reverses the section line direction. |
| [RotateByAngle](../SectionDrawingView/SectionDrawingView_RotateByAngle.md) | Method that rotates the drawing view by the specified angle. |
| [SetActiveModelState](../SectionDrawingView/SectionDrawingView_SetActiveModelState.md) | Method that sets the active model state for a drawing view. In this method users can also decide to update the PartsList objects which use the same model state as the drawing view. This method fails for drawing views where the model is unresolved. |
| [SetAutomatedCenterlineSettings](../SectionDrawingView/SectionDrawingView_SetAutomatedCenterlineSettings.md) | Method that sets the automatic centerline and center mark settings for this view and creates the centerlines and center marks defined by the settings. The centerlines and center marks that were created are returned. |
| [SetComponentLineColor](../SectionDrawingView/SectionDrawingView_SetComponentLineColor.md) | Method that sets color for a component in the drawing view. |
| [SetDesignViewRepresentation](../SectionDrawingView/SectionDrawingView_SetDesignViewRepresentation.md) | Method that sets a design view representation for a drawing view of an assembly. This method fails for drawing views of parts and presentations and in the case where the model (assembly) is unresolved. |
| [SetHiddenLinesStatus](../SectionDrawingView/SectionDrawingView_SetHiddenLinesStatus.md) | Method that sets the hidden lines status of a component in the drawing view. |
| [SetIncludeStatus](../SectionDrawingView/SectionDrawingView_SetIncludeStatus.md) | Method that sets the include status of the input object in the drawing view. This method automatically makes the object visible as well. After an object has been included, its visibility can be controlled using the GetVisibility and SetVisibility methods. |
| [SetVisibility](../SectionDrawingView/SectionDrawingView_SetVisibility.md) | Method that sets the visibility of the input object in the drawing view. |
| [SetWeldmentState](../SectionDrawingView/SectionDrawingView_SetWeldmentState.md) | Method that sets the weldment option for the drawing view. The method returns a failure if the referenced model does not contain weldments. |
| [SheetToDrawingViewSpace](../SectionDrawingView/SectionDrawingView_SheetToDrawingViewSpace.md) | Method that takes a 2d coordinate in sheet space, and returns a Point2d object containing the coordinate point in drawing view space. |
| [SheetToModelSpace](../SectionDrawingView/SectionDrawingView_SheetToModelSpace.md) | Method that takes a 2d coordinate in sheet space, and returns a Line in model space. Since this method transforms from 2D space to 3D space, there is insufficient information to obtain a 3D model point. Hence, this method returns a Line in the view direction on which the point lies. You may then use the FindUsingRay method to find the point(s) of interest. |
| [ShowHiddenAnnotations](../SectionDrawingView/SectionDrawingView_ShowHiddenAnnotations.md) | Method that displays all the annotations hidden by the user. |
| [ShowHiddenCurves](../SectionDrawingView/SectionDrawingView_ShowHiddenCurves.md) | Method that displays all the curves explicitly hidden by the user. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ActiveMemberName](../SectionDrawingView/SectionDrawingView_ActiveMemberName.md) | Gets and sets the name of the active member for a drawing view of an iPart or an iAssembly. |
| [ActiveModelState](../SectionDrawingView/SectionDrawingView_ActiveModelState.md) | Read-only property that gets the name of the active model state for a drawing view. This property returns a null string for drawing views of presentations and in the case where the model is unresolved. |
| [ActivePositionalRepresentation](../SectionDrawingView/SectionDrawingView_ActivePositionalRepresentation.md) | Gets and sets the name of the active Positional Representation for a drawing view of an assembly. |
| [ActivePresentationView](../SectionDrawingView/SectionDrawingView_ActivePresentationView.md) | Property that returns the name of the active Presentation (Exploded) View for a drawing view of a presentation. |
| [Aligned](../SectionDrawingView/SectionDrawingView_Aligned.md) | Gets and sets whether the view is aligned with another view. |
| [AttributeSets](../SectionDrawingView/SectionDrawingView_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [AuxiliaryOrientationEdge](../SectionDrawingView/SectionDrawingView_AuxiliaryOrientationEdge.md) | Property that returns drawing curve that the auxiliary view is aligned to. This property returns Nothing if this is not an auxiliary view or if the orientation edge (drawing curve) has been removed from the parent view during a subsequent update. |
| [BitmapAvailable](../SectionDrawingView/SectionDrawingView_BitmapAvailable.md) | Property that returns if this view's graphics are also available as a bitmap as well. If a bitmap exists it can be retrieved using the DataIO object. This is only applicable within Apprentice. |
| [BreakOperations](../SectionDrawingView/SectionDrawingView_BreakOperations.md) | Property that returns the BreakOperations object containing information about all the break operations applied to this view as well as methods to add breaks. Both local as well as inherited break operations are returned in the collection. |
| [BreakOutOperations](../SectionDrawingView/SectionDrawingView_BreakOutOperations.md) | Property that returns the BreakOutOperations object containing information about all the break out operations applied to this view as well as methods to add break outs. Only local break out operations are returned. |
| [Camera](../SectionDrawingView/SectionDrawingView_Camera.md) | Property that returns a Camera object that defines the orientation of the model within the view. |
| [Center](../SectionDrawingView/SectionDrawingView_Center.md) | Gets and sets the display center point of the drawing view on the owning sheet. |
| [ClientGraphicsCollection](../SectionDrawingView/SectionDrawingView_ClientGraphicsCollection.md) | Property that returns the ClientGraphicsCollection object. |
| [CropOperations](../SectionDrawingView/SectionDrawingView_CropOperations.md) | Read-only property that returns the CropOperations object containing information about all the crop operations applied to this view as well as methods to add crops. |
| [DataIO](../SectionDrawingView/SectionDrawingView_DataIO.md) | Property that returns the associated DataIO object. This can be used in Apprentice to obtain an associated bitmap, if it exists. |
| [DesignViewAssociative](../SectionDrawingView/SectionDrawingView_DesignViewAssociative.md) | Read-only property that gets whether the DesignViewRepresentation for a drawing view of a model is associative or not. |
| [DesignViewRepresentation](../SectionDrawingView/SectionDrawingView_DesignViewRepresentation.md) | Read-only property that returns the name of the Design View Representation for a drawing view of a model. |
| [DisplayBendExtents](../SectionDrawingView/SectionDrawingView_DisplayBendExtents.md) | Gets and sets whether to display sheet metal bend extents on the drawing view. |
| [DisplayDefinitionInBase](../SectionDrawingView/SectionDrawingView_DisplayDefinitionInBase.md) | Gets and sets whether to display detail circles, section lines and the associated text in the base view. |
| [DisplayForeshortenedTangentEdges](../SectionDrawingView/SectionDrawingView_DisplayForeshortenedTangentEdges.md) | Gets and sets whether to display shortened tangent edges in order to distinguish them from visible edges. |
| [DisplayHatching](../SectionDrawingView/SectionDrawingView_DisplayHatching.md) | Gets and sets whether to display hatches for section and slice views. |
| [DisplayInterferenceEdges](../SectionDrawingView/SectionDrawingView_DisplayInterferenceEdges.md) | Gets and sets whether to display both hidden edges that are excluded due to an interference condition (press, or interference fit conditions, threaded fasteners in tapped holes where the hole feature is modeled with the minor diameter). |
| [DisplayTangentEdges](../SectionDrawingView/SectionDrawingView_DisplayTangentEdges.md) | Read-write property that gets and sets whether to display the tangent edges on the drawing view. |
| [DisplayThreadFeatures](../SectionDrawingView/SectionDrawingView_DisplayThreadFeatures.md) | Gets and sets whether to display thread features on the drawing view. |
| [DisplayTrails](../SectionDrawingView/SectionDrawingView_DisplayTrails.md) | Gets and sets whether to display trails. |
| [DrawingCurves](../SectionDrawingView/SectionDrawingView_DrawingCurves.md) | Property that returns all the drawing curves within the drawing view optionally filtered to the input model object. This property returns Nothing for draft views.iew object represents a drawing view on a sheet. |
| [DrawingViewEvents](../SectionDrawingView/SectionDrawingView_DrawingViewEvents.md) | Property that returns the object, which provides event notifcation. For example, view updates. |
| [DrawingViewToModelTransform](../SectionDrawingView/SectionDrawingView_DrawingViewToModelTransform.md) | Property that returns the transformation from drawing view coordinate space to the model space. |
| [DrawingViewToSheetTransform](../SectionDrawingView/SectionDrawingView_DrawingViewToSheetTransform.md) | Property that returns the transformation from drawing view coordinate space to the sheet space. |
| [FullSectionDepth](../SectionDrawingView/SectionDrawingView_FullSectionDepth.md) | Property that gets and sets whether to section all geometry beyond the cutting line. If set to False, the SectionDepth property specifies a distance of viewing beginning from the cutting line. Setting the SectionDepth property automatically toggles this property to False. This property does not apply (and setting it returns an error) if the SliceAllParts property is set to True. |
| [GeneralDimensionType](../SectionDrawingView/SectionDrawingView_GeneralDimensionType.md) | Read-write property that indicates the type of dimension. |
| [GraphicsDataSetsCollection](../SectionDrawingView/SectionDrawingView_GraphicsDataSetsCollection.md) | Property that returns the object for the drawing view. |
| [HasOriginIndicator](../SectionDrawingView/SectionDrawingView_HasOriginIndicator.md) | Property that specifies whether the origin indicator for ordinate dimensions and hole tables has been created. |
| [HatchRegions](../SectionDrawingView/SectionDrawingView_HatchRegions.md) | Read-only property that returns the DrawingViewHatchRegions collection object. |
| [Height](../SectionDrawingView/SectionDrawingView_Height.md) | Property that specifies the height of the drawing view. The view height cannot be set but is defined by the contents of the view |
| [HiddenLineCalculationForAllBodies](../SectionDrawingView/SectionDrawingView_HiddenLineCalculationForAllBodies.md) | Read-write property that gets and sets whether the hidden line are calculated for all bodies or reference data separately. |
| [Include3DAnnotations](../SectionDrawingView/SectionDrawingView_Include3DAnnotations.md) | Read-write property that gets and sets whether to include the 3D annotations. |
| [IncludeMeshBodies](../SectionDrawingView/SectionDrawingView_IncludeMeshBodies.md) | Read-write property that gets and sets whether to include the mesh bodies. |
| [IncludeSlice](../SectionDrawingView/SectionDrawingView_IncludeSlice.md) | Property that gets and sets whether some components are sliced and some components are sectioned, depending on their individual settings. |
| [IncludeSurfaceBodies](../SectionDrawingView/SectionDrawingView_IncludeSurfaceBodies.md) | Read-write property that gets and sets whether to include the work surfaces. |
| [InheritBreak](../SectionDrawingView/SectionDrawingView_InheritBreak.md) | Gets and sets whether the view should inherit the corresponding break from the parent view. |
| [InheritBreakOut](../SectionDrawingView/SectionDrawingView_InheritBreakOut.md) | Gets and sets whether the view should inherit the corresponding break out from the parent view. |
| [InheritSection](../SectionDrawingView/SectionDrawingView_InheritSection.md) | Gets and sets whether the view should inherit the corresponding section cut from the parent view. |
| [InheritSlice](../SectionDrawingView/SectionDrawingView_InheritSlice.md) | Gets and sets whether the view should inherit the corresponding slice cut from the parent view. |
| [IsBreakLineSmooth](../SectionDrawingView/SectionDrawingView_IsBreakLineSmooth.md) | Read-write property that gets and sets whether the cut edges are smooth or jogged. |
| [IsFlatPatternView](../SectionDrawingView/SectionDrawingView_IsFlatPatternView.md) | Gets whether the drawing view is of a sheet metal flat pattern. |
| [IsRasterView](../SectionDrawingView/SectionDrawingView_IsRasterView.md) | Read-write property that gets and sets whether the drawing view is raster view or not. |
| [IsTextPropertySource](../SectionDrawingView/SectionDrawingView_IsTextPropertySource.md) | Read-write property that gets and sets whether the drawing view is specified as the text property source.This is applicable only when the drawing view is a base view. |
| [IsUpdateComplete](../SectionDrawingView/SectionDrawingView_IsUpdateComplete.md) | Indicates if the view has finished updating. |
| [Label](../SectionDrawingView/SectionDrawingView_Label.md) | Property that returns the DrawingViewLabel object. |
| [Left](../SectionDrawingView/SectionDrawingView_Left.md) | Property that returns the position of the left edge of the drawing view. |
| [Margin](../SectionDrawingView/SectionDrawingView_Margin.md) | Read-write property that gets and sets the amount of area outside the normal view boundary that the view boundary extends. |
| [ModelToDrawingViewTransform](../SectionDrawingView/SectionDrawingView_ModelToDrawingViewTransform.md) | Property that returns the transformation from model space to the drawing view coordinate space. |
| [ModelToSheetTransform](../SectionDrawingView/SectionDrawingView_ModelToSheetTransform.md) | Property that returns the transformation from model space to the sheet coordinate space. |
| [Name](../SectionDrawingView/SectionDrawingView_Name.md) | Gets or sets the name of this View. |
| [OriginIndicator](../SectionDrawingView/SectionDrawingView_OriginIndicator.md) | Property that gets the origin indicator for ordinate dimensions and hole tables. |
| [Parent](../SectionDrawingView/SectionDrawingView_Parent.md) | Property returning the parent Sheet object. |
| [ParentView](../SectionDrawingView/SectionDrawingView_ParentView.md) | Property that returns the parent . This property returns Nothing in the case where no parent view exists. |
| [Position](../SectionDrawingView/SectionDrawingView_Position.md) | Gets and sets the point used to position the drawing view on the sheet. |
| [PresentationViewAssociative](../SectionDrawingView/SectionDrawingView_PresentationViewAssociative.md) | Gets and sets whether to associate the drawing view to the referenced presentation view. |
| [ReferenceDataDisplayStyle](../SectionDrawingView/SectionDrawingView_ReferenceDataDisplayStyle.md) | Read-write property that gets and sets the reference data display style. |
| [ReferencedDocumentDescriptor](../SectionDrawingView/SectionDrawingView_ReferencedDocumentDescriptor.md) | Property that returns the model document referenced by this view. |
| [RevisionClouds](../SectionDrawingView/SectionDrawingView_RevisionClouds.md) | Returns the collection of revision clouds on this drawing view. |
| [Rotation](../SectionDrawingView/SectionDrawingView_Rotation.md) | Read-write property that gets and sets the absolute rotation angle of the drawing view in radians. The value can either be positive (counter-clockwise rotation) or negative (clockwise rotation). |
| [Scale](../SectionDrawingView/SectionDrawingView_Scale.md) | Gets or sets the Model-to-PaperSpace scale of this particular Drawing View. |
| [ScaleFromBase](../SectionDrawingView/SectionDrawingView_ScaleFromBase.md) | Gets and sets whether the scale of the view derives from the parent view or not. |
| [ScaleString](../SectionDrawingView/SectionDrawingView_ScaleString.md) | Gets or sets the Model-to-PaperSpace scale in string format of this particular Drawing View. |
| [SectionDepth](../SectionDrawingView/SectionDrawingView_SectionDepth.md) | Property that gets and sets the section depth in centimeters. Setting this property automatically toggles the FullSectionDepth property to False. Setting the property to a value between 0 and 0.00003 sets the depth to the smallest available section depth value of 0.00003. This property does not apply (and setting it returns an error) if the SliceAllParts property is set to True. |
| [SectionLineSketch](../SectionDrawingView/SectionDrawingView_SectionLineSketch.md) | Gets the object that contains the profile used to define the section line of the view. |
| [SheetToDrawingViewTransform](../SectionDrawingView/SectionDrawingView_SheetToDrawingViewTransform.md) | Property that returns the transformation from sheet space to the drawing view coordinate space. |
| [SheetToModelTransform](../SectionDrawingView/SectionDrawingView_SheetToModelTransform.md) | Property that returns the transformation from sheet coordinate space to the model space. |
| [ShowEntireLine](../SectionDrawingView/SectionDrawingView_ShowEntireLine.md) | Property that indicates whether to show the entire section line or hide parts of it. |
| [ShowLabel](../SectionDrawingView/SectionDrawingView_ShowLabel.md) | Gets and sets whether to show the label of the drawing view on the sheet. |
| [ShowTrails](../SectionDrawingView/SectionDrawingView_ShowTrails.md) | Gets and set whether to show the trails or not for a drawing view of a presentation. |
| [Sketches](../SectionDrawingView/SectionDrawingView_Sketches.md) | Property that returns the DrawingSketches collection object for the sheet. This object provides access to all of the sketches that have been created on the sheet and provides functionality to create new sketches. |
| [SliceAllParts](../SectionDrawingView/SectionDrawingView_SliceAllParts.md) | Property that gets and sets whether to override all individual settings and slice all components in the view according to the Section Line geometry. Components that are not crossed by the Section Line will not participate in the resulting view. Setting this property to True automatically toggles the IncludeSlice property to True. This property does not apply (and setting it returns an error) for drawing views of a part. |
| [StandardPartsSectionBehavior](../SectionDrawingView/SectionDrawingView_StandardPartsSectionBehavior.md) | Gets and sets the sectioning behavior for standard parts in drawing views of assemblies. |
| [Suppressed](../SectionDrawingView/SectionDrawingView_Suppressed.md) | Gets and sets whether this drawing view is suppressed or not. |
| [Top](../SectionDrawingView/SectionDrawingView_Top.md) | Property that specifies the position of the top edge of the drawing view. |
| [Type](../SectionDrawingView/SectionDrawingView_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UpToDate](../SectionDrawingView/SectionDrawingView_UpToDate.md) | Property that returns whether the drawing view is up to date with respect to the model. |
| [UseAlignedMethod](../SectionDrawingView/SectionDrawingView_UseAlignedMethod.md) | Property that gets and sets whether to use the projected or the aligned method. |
| [ViewAnnotation](../SectionDrawingView/SectionDrawingView_ViewAnnotation.md) | Read-only property that returns the drawing view annotation object. |
| [ViewJustification](../SectionDrawingView/SectionDrawingView_ViewJustification.md) | Gets and sets the view justification. |
| [ViewOrientationFromBase](../SectionDrawingView/SectionDrawingView_ViewOrientationFromBase.md) | Gets and sets whether the view should inherit the orientation from the base view. |
| [ViewStyle](../SectionDrawingView/SectionDrawingView_ViewStyle.md) | Gets and sets the drawing view style. |
| [ViewType](../SectionDrawingView/SectionDrawingView_ViewType.md) | Property returning an DrawingViewTypeEnum constant indicating the type of view. |
| [Width](../SectionDrawingView/SectionDrawingView_Width.md) | Property that specifies the width of the drawing view. The view width cannot be set but is defined by the contents of the view. |

## Accessed From

[DrawingViews.AddSectionView](../DrawingViews/DrawingViews_AddSectionView.md), [DrawingViews.AddSectionView2](../DrawingViews/DrawingViews_AddSectionView2.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Break alignment of a section view](../../sample-programs/SectionDrawingView_Sample.md) | Sample showing how to break the alignment of a drawing section view by calling the DrawingBreakViewAlignment command. |

## Version

Introduced in version 9
