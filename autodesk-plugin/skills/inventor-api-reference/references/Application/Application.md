# Application Object

Derived from: [InventorServerObject](InventorServerObject.md) Object

## Description

Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConstructInternalNameAndRevisionId](../Application/Application_ConstructInternalNameAndRevisionId.md) | Constructs and returns the Internal Name and Revision Identifier |
| [CreateFactoryTableDialog](../Application/Application_CreateFactoryTableDialog.md) | Creates a Factory Table dialog. |
| [CreateFileDialog](../Application/Application_CreateFileDialog.md) | Method that creates a new FileDialog object. The FileDialog object is similar to the Microsoft common dialog control and allows you to reuse the Inventor open and save dialogs. |
| [CreateProgressBar](../Application/Application_CreateProgressBar.md) | Method that creates a new ProgressBar object. The progress bar is not immediately displayed. Calling the UpdateProgress method for the first time causes the bar to display. |
| [ExportApplicationOptions](../Application/Application_ExportApplicationOptions.md) | Method that exports the Application Options to an XML file. |
| [GetAppFrameExtents](../Application/Application_GetAppFrameExtents.md) | Obtains the position and size of the application's main frame window. |
| [GetInterfaceObject](../Application/Application_GetInterfaceObject.md) | Constructs and returns the IUnknown object for the specified ProgID or CLSID. |
| [GetInterfaceObject32](../Application/Application_GetInterfaceObject32.md) | In 32-bit Autodesk Inventor, this method always returns the same object as GetInterfaceObject. |
| [GetMaterialXFromAsset](../Application/Application_GetMaterialXFromAsset.md) | Method that gets the MaterialX string from an Asset. |
| [GetMDIClientAreaExtents](../Application/Application_GetMDIClientAreaExtents.md) | Obtains the position and size of the Application's MDI client area. |
| [ImportApplicationOptions](../Application/Application_ImportApplicationOptions.md) | Method that imports the Application Options from an XML file. |
| [Move](../Application/Application_Move.md) | Method that moves the frame window. |
| [Quit](../Application/Application_Quit.md) | Shuts down the application. |
| [RefreshRibbonForComparison](../Application/Application_RefreshRibbonForComparison.md) | Method that refreshes the ribbon controls display when the comparison is set. |
| [ReserveLicense](../Application/Application_ReserveLicense.md) | Informs Inventor/Apprentice that a license should be retained for this instance of the application. Used to prevent idle detection from returning the seat license to the license pool. Requires a call to UnreserveLicense with the same ClientID to allow license reclamation to resume. |
| [UnreserveLicense](../Application/Application_UnreserveLicense.md) | Informs Inventor/Apprentice that normal seat license reclamation can resume. Use this method when extended processing for which a license was reserved completes. Do not use without a previous call to ReserveLicense using the same ClientID. |
| [UseAutoCADRelatedSettings](../Application/Application_UseAutoCADRelatedSettings.md) | Method that sets the Application Options using AutoCAD related settings. |
| [UseInventorSettings](../Application/Application_UseInventorSettings.md) | Method that sets the Application Options using Inventor Settings. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ActiveAppearanceLibrary](../Application/Application_ActiveAppearanceLibrary.md) | Read-write property that gets and sets the library whose contents is listed in the appearances drop-down list in the QAT (Quick Access Toolbar)\_at the top of the Inventor window. The initial active appearance is defined by the active project. Using this property you can override the project appearance. When a new project is activated the active appearance will be determined by the activated project. |
| [ActiveColorScheme](../Application/Application_ActiveColorScheme.md) | Property that returns the ColorScheme that is currently active. |
| [ActiveDocument](../Application/Application_ActiveDocument.md) | Gets the active Document. |
| [ActiveDocumentType](../Application/Application_ActiveDocumentType.md) | Gets the type of the active document. |
| [ActiveEditDocument](../Application/Application_ActiveEditDocument.md) | Property that returns the current in-place editing document. |
| [ActiveEditObject](../Application/Application_ActiveEditObject.md) | Gets the object that is currently open for edit within the Autodesk Inventor user interface. |
| [ActiveMaterialLibrary](../Application/Application_ActiveMaterialLibrary.md) | Gets and sets the library whose contents is listed in the materials drop-down list in the QAT(Quick Access Toolbar) at the top of the Inventor window. |
| [ActiveView](../Application/Application_ActiveView.md) | Gets the active view. |
| [ActiveViewFrame](../Application/Application_ActiveViewFrame.md) | Read-only property that returns the active ViewFrame object. |
| [ApplicationAddIns](../Application/Application_ApplicationAddIns.md) | Property that returns the ApplicationAddIns object. This object provides access to the Add-Ins currently installed. |
| [ApplicationEvents](../Application/Application_ApplicationEvents.md) | Property that returns the ApplicationEvents object. This object supports a set of events that are application-centric. |
| [AssemblyEvents](../Application/Application_AssemblyEvents.md) | Property that returns the AssemblyEvents object. This object supports a set of events that are assembly centric. |
| [AssemblyOptions](../Application/Application_AssemblyOptions.md) | Property that returns the AssemblyOptions object. The AssemblyOptions object provides access to various assembly related application level options. This is somewhat equivalent to the Assembly tab of the Application Options dialog. |
| [AssetLibraries](../Application/Application_AssetLibraries.md) | Gets AssetLibraries collection object. This collection provides access to the all of the appearance and material libraries. |
| [AvailableComparisonVersions](../Application/Application_AvailableComparisonVersions.md) | Read-only property that returns an array of strings indicating the versions can be used to compare the commands with selected version. |
| [CameraEvents](../Application/Application_CameraEvents.md) | Gets the object that fires the Camera related events. |
| [Caption](../Application/Application_Caption.md) | Gets/Sets the caption on the Application's frame window. |
| [ChangeManager](../Application/Application_ChangeManager.md) | Gets the ChangeManager object. The ChangeManager object manages the processes involved in making changes to data and recording the change process. |
| [ClientOperationEvents](../Application/Application_ClientOperationEvents.md) | Read-only property that returns the ClientOperationEvents object. |
| [ClientResourceMaps](../Application/Application_ClientResourceMaps.md) | Read-only property that returns ClientResourceMaps object. |
| [ColorSchemes](../Application/Application_ColorSchemes.md) | Property that returns the ColorSchemes object. The ColorSchemes object provides access to the color schemes. This is somewhat equivalent to the Colors tab of the Application Options dialog. |
| [CommandManager](../Application/Application_CommandManager.md) | Property that returns the CommandManager object. |
| [ComparisonVersion](../Application/Application_ComparisonVersion.md) | Read-write property that gets and sets the comparison version for commands. When set a comparison version, the commands will show additional info against the version (like whether a command is introduced/updated later than the version). The AvailableComparison. |
| [ContentCenter](../Application/Application_ContentCenter.md) | Property that returns the ContentCenter object. |
| [ContentCenterOptions](../Application/Application_ContentCenterOptions.md) | Returns the ContentCenterOptions object. |
| [DesignProjectManager](../Application/Application_DesignProjectManager.md) | Gets the design project manager object. |
| [DisplayOptions](../Application/Application_DisplayOptions.md) | Gets the Display Options. |
| [Documents](../Application/Application_Documents.md) | Gets all the in-memory documents in a collection. |
| [DrawingOptions](../Application/Application_DrawingOptions.md) | Property that returns the DrawingOptions object. The DrawingOptions object provides access to various drawing related application level options. This is somewhat equivalent to the Drawing tab of the Application Options dialog. |
| [ErrorManager](../Application/Application_ErrorManager.md) | Property that returns the ErrorManager object. This object can be used to get errors that occurred during an API call, add to Inventor's errors or to display them. |
| [FavoriteAssets](../Application/Application_FavoriteAssets.md) | Gets the set of favorite assets. This includes both appearance and material assets. |
| [FileAccessEvents](../Application/Application_FileAccessEvents.md) | Property that returns the FileAccessEvents object. This object supports a set of events that are fired as a result of a file being accessed. |
| [FileManager](../Application/Application_FileManager.md) | Property that returns the FileManager object. |
| [FileOptions](../Application/Application_FileOptions.md) | Property that returns the FileOptions object. The FileOptions object provides access to various file related application level options. This is somewhat equivalent to the File tab of the Application Options dialog. |
| [FileUIEvents](../Application/Application_FileUIEvents.md) | Property that returns the FileUIEvents object. This object supports a set of events that are fired in reaction to certain user interface actions. |
| [GeneralOptions](../Application/Application_GeneralOptions.md) | Property that returns the GeneralOptions object. The GeneralOptions object provides access to various application level options. This is somewhat equivalent to the General tab of the Application Options dialog. |
| [HardwareOptions](../Application/Application_HardwareOptions.md) | Gets the Hardware Options. |
| [Height](../Application/Application_Height.md) | Gets/Sets Height edge of the frame window. |
| [HelpManager](../Application/Application_HelpManager.md) | Gets the HelpManager object that provides access to the help-related activity taking place in the system. |
| [iFeatureOptions](../Application/Application_iFeatureOptions.md) | Property that returns the iFeatureOptions object. The iFeatureOptions object provides access to various iFeature related application level options. This is somewhat equivalent to the iFeature tab of the Application Options dialog. |
| [InstallPath](../Application/Application_InstallPath.md) | Property that returns the full path where Inventor/Apprentice is installed. |
| [IsIn3dPrintMode](../Application/Application_IsIn3dPrintMode.md) | Read-only property that indicates whether Application is in 3D print preview mode. |
| [LanguageCode](../Application/Application_LanguageCode.md) | Read-only property that returns the language code used to describe the current language being used by Inventor. The code is returned in the form of an EITF language code. The following codes can be returned by Inventor:  * Brazilian Portuguese: pt-BR * Czech: cs-CZ * English: en-US * French: fr-FR * German: de-DE * Italian: it-IT * Japanese: ja-JP * Korean: ko-KR * Polish: pl-PL * Russian: ru-RU * Simplified Chinese: zh-CN * Spanish: es-ES * Traditional Chinese: zh-TW |
| [LanguageName](../Application/Application_LanguageName.md) | Gets the language currently in use in Autodesk Inventor. |
| [LanguageTools](../Application/Application_LanguageTools.md) | Property that returns the LanguageTools object. |
| [Left](../Application/Application_Left.md) | Gets/Sets the distance between the left edge of the screen and left edge of the frame window. |
| [Locale](../Application/Application_Locale.md) | Property that returns the Locale Id currently in use in Autodesk Inventor, along with a string name of the language. Calling GetLocaleInfo with the LocaleId should give you further information. |
| [LoggedIn](../Application/Application_LoggedIn.md) | Read-only property that returns whether a user has logged in the online services or not. |
| [LoginUserId](../Application/Application_LoginUserId.md) | Read-only property that returns the login user Id(this is the same as the A360 oxygen Id). This returns empty string if has not logged in. |
| [LoginUserName](../Application/Application_LoginUserName.md) | Read-only property that returns the online services login user name. This returns empty string if has not logged in. |
| [MainFrameHWND](../Application/Application_MainFrameHWND.md) | Gets the Application main window's HWND. |
| [MaterialDisplayUnits](../Application/Application_MaterialDisplayUnits.md) | Gets and sets the units that are used in the user interface when working with materials. |
| [MeasureTools](../Application/Application_MeasureTools.md) | Returns the MeasureTools object. |
| [ModelingEvents](../Application/Application_ModelingEvents.md) | Property that returns the ModelingEvents object. This object supports a set of events that are common to parts and assemblies. |
| [ModelStateEvents](../Application/Application_ModelStateEvents.md) | Read-only property that returns the ModelStateEvents object. |
| [MRUDisplay](../Application/Application_MRUDisplay.md) | Gets/Sets the property that turns display of the application's MRU list on and off. |
| [MRUEnabled](../Application/Application_MRUEnabled.md) | Gets/Sets the property that deals with the application's ability to add files to the MRU list. |
| [NotebookOptions](../Application/Application_NotebookOptions.md) | Property that returns the NotebookOptions object. The NotebookOptions object provides access to various notebook related application level options. This is somewhat equivalent to the Notebook tab of the Application Options dialog. |
| [OpenDocumentsDisplay](../Application/Application_OpenDocumentsDisplay.md) | Gets/Sets the property that turns display of the application's Open Documents list on and off. |
| [PartOptions](../Application/Application_PartOptions.md) | Property that returns the PartOptions object. The PartOptions object provides access to various part related application level options. This is somewhat equivalent to the Part tab of the Application Options dialog. |
| [PresentationOptions](../Application/Application_PresentationOptions.md) | Gets the Presentation Options. |
| [PromptsOptions](../Application/Application_PromptsOptions.md) | Gets the Prompts Options object. |
| [Ready](../Application/Application_Ready.md) | Boolean property indicating whether Inventor has completed its initialization. This includes initialization of all the Add-ins loaded at startup.This property should be used in conjunction with the ApplicationEvents.OnReady event. |
| [RepresentationEvents](../Application/Application_RepresentationEvents.md) | Property that returns the RepresentationEvents object. This object supports a set of events related to design view and positional representations that are assembly centric. |
| [SaveOptions](../Application/Application_SaveOptions.md) | Property that returns the SaveOptions object. The SaveOptions object provides access to various save related application level options. This is somewhat equivalent to the Save tab of the Application Options dialog. |
| [ScreenUpdating](../Application/Application_ScreenUpdating.md) | Gets and sets whether the screen is updated (redrawn) during a series of actions. Turn off screen updating while a series of actions are performed so that the screen is not redrawn after each action. Remember to turn screen updating on to update the screen. |
| [SilentOperation](../Application/Application_SilentOperation.md) | Gets/Sets the Boolean flag that controls whether an operation will proceed without prompting (if that gets required...e.g.: error message dismissal). If Inventor is running visible, this property is FALSE by default. |
| [SketchEvents](../Application/Application_SketchEvents.md) | Property that returns the SketchEvents object. This object supports a set of 2d and 3d sketch-related events that are common to parts, assemblies and drawings. |
| [SketchOptions](../Application/Application_SketchOptions.md) | Property that returns the SketchOptions object. The SketchOptions object provides access to various 2D sketch related application level options. This is somewhat equivalent to the 2D Sketch portion on the Sketch tab of the Application Options dialog. |
| [SoftwareVersion](../Application/Application_SoftwareVersion.md) | Gets the object that encapsulates the version of the current software. |
| [StatusBarText](../Application/Application_StatusBarText.md) | Gets/Sets the Status Bar text in first pane of the Application's Main frame. |
| [StyleEvents](../Application/Application_StyleEvents.md) | Property that returns the StyleEvents object. This object supports a set of events that relate to styles. |
| [StylesManager](../Application/Application_StylesManager.md) | Gets the StylesManager object. |
| [SupportsFileManagement](../Application/Application_SupportsFileManagement.md) | Gets/Sets whether a file management AddIn is present. |
| [ThemeManager](../Application/Application_ThemeManager.md) | Gets the ThemeManager object. |
| [Top](../Application/Application_Top.md) | Gets/Sets the distance between the top of the screen and top of the frame window. |
| [TransactionManager](../Application/Application_TransactionManager.md) | Gets the TransactionManager object that controls all the database transactions taking place in the system. |
| [TransientBRep](../Application/Application_TransientBRep.md) | Property that returns the TransientBRep object. |
| [TransientGeometry](../Application/Application_TransientGeometry.md) | Gets the object through which all transient geometry objects can be constructed. |
| [TransientObjects](../Application/Application_TransientObjects.md) | Gets the object through which all general transient objects are created. |
| [Type](../Application/Application_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UnitsOfMeasure](../Application/Application_UnitsOfMeasure.md) | Property that returns the UnitsOfMeasure object. |
| [UserInterfaceManager](../Application/Application_UserInterfaceManager.md) | Gets the UserInterfaceManager object. The UserInterfaceManager object is the starting point for UI and environment control, providing access to available environments, command bars, browsers, panel bars, toolbars etc. |
| [UserName](../Application/Application_UserName.md) | Gets/sets the string that identifies the current user. Autodesk Inventor saves its own copy of this name per user and can thus be manipulated without affecting the rest of the OS. |
| [VBAProjects](../Application/Application_VBAProjects.md) | Property that returns Autodesk Inventor's VBA projects collection. |
| [VBE](../Application/Application_VBE.md) | Gets the top-level automation pointer to VBA's IDE. |
| [ViewFrames](../Application/Application_ViewFrames.md) | Read-only property that returns the ViewFramesEnumerator collection object. |
| [Views](../Application/Application_Views.md) | Gets all the open Views in a collection. |
| [Visible](../Application/Application_Visible.md) | Gets/Sets the visibility of this application. |
| [WebBrowserDialogs](../Application/Application_WebBrowserDialogs.md) | Read-only property that returns the WebBrowserDialogs collection object. |
| [Width](../Application/Application_Width.md) | Gets/Sets the Width the frame window. |
| [WindowState](../Application/Application_WindowState.md) | Gets/Sets the frame windows state. |

## Accessed From

[ApplicationAddInSite.Application](../ApplicationAddInSite/ApplicationAddInSite_Application.md), [AuxiliaryFeatureIndicator.Application](../AuxiliaryFeatureIndicator/AuxiliaryFeatureIndicator_Application.md), [AuxiliaryFeatureIndicators.Application](../AuxiliaryFeatureIndicators/AuxiliaryFeatureIndicators_Application.md), [BalloonTip.Application](../BalloonTip/BalloonTip_Application.md), [BalloonTips.Application](../BalloonTips/BalloonTips_Application.md), [BrowserFoldersEnumerator.Application](../BrowserFoldersEnumerator/BrowserFoldersEnumerator_Application.md), [BrowserNodesEnumerator.Application](../BrowserNodesEnumerator/BrowserNodesEnumerator_Application.md), [ButtonDefinition.Application](../ButtonDefinition/ButtonDefinition_Application.md), [ClientResourceMap.Parent](../ClientResourceMap/ClientResourceMap_Parent.md), [ComboBoxDefinition.Application](../ComboBoxDefinition/ComboBoxDefinition_Application.md), [CommandBar.Application](CommandBar_Application.md), [CommandBar.Parent](CommandBar_Parent.md), [CommandBarBaseCollection.Application](CommandBarBaseCollection_Application.md), [CommandBarButton.Application](CommandBarButton_Application.md), [CommandBarControl.Application](CommandBarControl_Application.md), [CommandBarControls.Application](CommandBarControls_Application.md), [CommandBarList.Application](CommandBarList_Application.md), [CommandBarPopUp.Application](CommandBarPopUp_Application.md), [CommandBars.Application](CommandBars_Application.md), [CommandCategories.Application](../CommandCategories/CommandCategories_Application.md), [CommandCategory.Application](../CommandCategory/CommandCategory_Application.md), [CommandControl.Application](../CommandControl/CommandControl_Application.md), [CommandControls.Application](../CommandControls/CommandControls_Application.md), [CommandControlsEnumerator.Application](../CommandControlsEnumerator/CommandControlsEnumerator_Application.md), [CommandManager.Parent](../CommandManager/CommandManager_Parent.md), [ControlDefinition.Application](../ControlDefinition/ControlDefinition_Application.md), [ControlDefinitionEvents.Application](ControlDefinitionEvents_Application.md), [ControlDefinitions.Application](../ControlDefinitions/ControlDefinitions_Application.md), [DisabledCommandList.Application](../DisabledCommandList/DisabledCommandList_Application.md), [Environment.Application](../Environment/Environment_Application.md), [Environment.Parent](../Environment/Environment_Parent.md), [EnvironmentBase.Application](EnvironmentBase_Application.md), [EnvironmentBase.Parent](EnvironmentBase_Parent.md), [EnvironmentBaseCollection.Application](EnvironmentBaseCollection_Application.md), [EnvironmentList.Application](../EnvironmentList/EnvironmentList_Application.md), [EnvironmentManager.Application](../EnvironmentManager/EnvironmentManager_Application.md), [Environments.Application](../Environments/Environments_Application.md), [FileUIEvents.Application](../FileUIEvents/FileUIEvents_Application.md), [FileUIEvents.Parent](../FileUIEvents/FileUIEvents_Parent.md), [InteractionEvents.Application](../InteractionEvents/InteractionEvents_Application.md), [InventorVBAProject.Parent](../InventorVBAProject/InventorVBAProject_Parent.md), [InventorVBAProjects.Parent](../InventorVBAProjects/InventorVBAProjects_Parent.md), [KeyboardEvents.Application](../KeyboardEvents/KeyboardEvents_Application.md), [LicenseManager.Application](../LicenseManager/LicenseManager_Application.md), [LicenseManager.Parent](../LicenseManager/LicenseManager_Parent.md), [MacroControlDefinition.Application](../MacroControlDefinition/MacroControlDefinition_Application.md), [ManipulatorEvents.Application](../ManipulatorEvents/ManipulatorEvents_Application.md), [MeasureEvents.Application](../MeasureEvents/MeasureEvents_Application.md), [MiniToolbar.Application](../MiniToolbar/MiniToolbar_Application.md), [MiniToolbarButton.Application](../MiniToolbarButton/MiniToolbarButton_Application.md), [MiniToolbarCheckBox.Application](../MiniToolbarCheckBox/MiniToolbarCheckBox_Application.md), [MiniToolbarComboBox.Application](../MiniToolbarComboBox/MiniToolbarComboBox_Application.md), [MiniToolbarControl.Application](../MiniToolbarControl/MiniToolbarControl_Application.md), [MiniToolbarControls.Application](../MiniToolbarControls/MiniToolbarControls_Application.md), [MiniToolbarDropdown.Application](../MiniToolbarDropdown/MiniToolbarDropdown_Application.md), [MiniToolbarSlider.Application](../MiniToolbarSlider/MiniToolbarSlider_Application.md), [MiniToolbarTextBox.Application](../MiniToolbarTextBox/MiniToolbarTextBox_Application.md), [MiniToolbarTextEditor.Application](MiniToolbarTextEditor_Application.md), [MiniToolbarValueEditor.Application](../MiniToolbarValueEditor/MiniToolbarValueEditor_Application.md), [ModelDatumReferenceFrame.Application](ModelDatumReferenceFrame_Application.md), [ModelDatumReferenceFrameDefinition.Application](ModelDatumReferenceFrameDefinition_Application.md), [ModelDatumReferenceFrameProxy.Application](ModelDatumReferenceFrameProxy_Application.md), [ModelDatumReferenceFrames.Application](ModelDatumReferenceFrames_Application.md), [ModelToleranceFeatureDefinition.Application](ModelToleranceFeatureDefinition_Application.md), [MouseEvents.Application](../MouseEvents/MouseEvents_Application.md), [PanelBar.Application](PanelBar_Application.md), [ProgressiveToolTip.Application](../ProgressiveToolTip/ProgressiveToolTip_Application.md), [ProjectOptionsButton.Application](../ProjectOptionsButton/ProjectOptionsButton_Application.md), [PublicationMeshEdge.Application](PublicationMeshEdge_Application.md), [PublicationMeshFace.Application](PublicationMeshFace_Application.md), [RadialMarkingMenu.Application](../RadialMarkingMenu/RadialMarkingMenu_Application.md), [RadialMarkingMenus.Application](../RadialMarkingMenus/RadialMarkingMenus_Application.md), [Ribbon.Application](../Ribbon/Ribbon_Application.md), [RibbonPanel.Application](../RibbonPanel/RibbonPanel_Application.md), [RibbonPanels.Application](../RibbonPanels/RibbonPanels_Application.md), [Ribbons.Application](../Ribbons/Ribbons_Application.md), [RibbonTab.Application](../RibbonTab/RibbonTab_Application.md), [RibbonTabs.Application](../RibbonTabs/RibbonTabs_Application.md), [SelectEvents.Application](../SelectEvents/SelectEvents_Application.md), [Theme.Application](../Theme/Theme_Application.md), [ThemeManager.Application](../ThemeManager/ThemeManager_Application.md), [ThemeManager.Parent](../ThemeManager/ThemeManager_Parent.md), [ThemesEnumerator.Application](../ThemesEnumerator/ThemesEnumerator_Application.md), [TriadEvents.Application](../TriadEvents/TriadEvents_Application.md), [TutorialsManager.Parent](TutorialsManager_Parent.md), [UserInputEvents.Application](../UserInputEvents/UserInputEvents_Application.md), [UserInterfaceEvents.Application](../UserInterfaceEvents/UserInterfaceEvents_Application.md), [UserInterfaceManager.Application](../UserInterfaceManager/UserInterfaceManager_Application.md), [UserInterfaceManager.Parent](../UserInterfaceManager/UserInterfaceManager_Parent.md), [VbaApplication.ThisApplication](../VbaApplication/VbaApplication_ThisApplication.md), [ViewFrame.Application](../ViewFrame/ViewFrame_Application.md), [ViewFrame.Parent](../ViewFrame/ViewFrame_Parent.md), [ViewFramesEnumerator.Application](../ViewFramesEnumerator/ViewFramesEnumerator_Application.md), [WebBrowserDialog.Application](../WebBrowserDialog/WebBrowserDialog_Application.md), [WebView.Application](WebView_Application.md)

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |