# Quickstart guide

This article provides a quick guide to getting started with KoboToolbox. It explains how to create an account, build and deploy a form, and begin collecting data.

<iframe src="https://www.youtube.com/embed/CYJ-Ob_7Ql8?si=SDjFjZF4zQBE-thP" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>



## Creating an account and signing in
To get started, go to the [Sign up page](https://www.kobotoolbox.org/sign-up/) and create an account on one of our public servers. Most users sign up for an account on our [Global KoboToolbox Server](https://kf.kobotoolbox.org/). Users and organizations that require or prefer data hosting in the European Union can sign up for an account on the [European Union KoboToolbox Server](https://eu.kobotoolbox.org/).

Activate your account using the emailed link, then sign in via the server URL or the [Sign up page](https://www.kobotoolbox.org/sign-up/). 

<p class="note">
    For more information about creating an account, see <a href="https://support.kobotoolbox.org/creating_account.html">Creating an account on KoboToolbox</a>.
</p>


## Creating your first project

To create your first form:
1. Click on **{{ui:new|upper}}**. You will be prompted to choose a project source.

| Option                    | Description                                                                                                           |
| :------------------------ | :-------------------------------------------------------------------------------------------------------------------- |
| {{ui:Build from scratch}}        | Build a form using the KoboToolbox <a href="formbuilder.html" class="reference">Formbuilder</a>.                   |
| {{ui:Use a template}}            | Build a form using a template from the <a href="question_library.html" class="reference">question library</a>.   |
| {{ui:Upload}} XLSForm            | {{ui:Upload}} an <a href="edit_forms_excel.html" class="reference">XLSForm</a> file where you have defined your questions.     |
| Import an XLSForm via URL | {{ui:Upload}} an XLSForm file <a href="https://support.kobotoolbox.org/xlsform_with_kobotoolbox.html#importing-an-xlsform-via-url" class="reference">from an online source</a> such as Google Drive or Dropbox. |


2. Select **{{ui:Build from scratch}}** to create a new form using the KoboToolbox Formbuilder.
3. In the **Project details** dialog box, enter the relevant information about your project and then click **{{ui:Create project|bold}}**.

## Building a form using the Formbuilder

1. Once in the Formbuilder, click the <i class="k-icon-plus"></i> button to add your first question. Enter the question label and choose a [question type](question_types.md).
2. To specify question parameters, click the <i class="k-icon-settings"></i> **{{ui:Settings}}** icon. For example, you can make a question required, change its appearance, or add [skip logic](skip_logic.md) conditions.
3. Click <i class="k-icon-view"></i> **{{ui:Preview form}}** to view and test your form.
4. To save the form, click **{{ui:Save}}** in the top right corner, then click <i class="k-icon-close"></i> to close the form.

<p class="note">
    To learn more about using the Formbuilder, see <a href="https://support.kobotoolbox.org/formbuilder.html">Getting started with the KoboToolbox Formbuilder</a> and <a href="https://support.kobotoolbox.org/question_options.html">Using the question options</a>.
</p>


## Deploying your form for data collection

1. To start collecting data, click **{{ui:deploy|upper}}** in the **{{ui:form|upper}}** page to [deploy your draft form](deploy_form_new_project.md) as a new data collection project.
2. Under **{{ui:Collect data}}**, click **{{ui:Copy}}** to share the form link for data entry [from a browser](data_through_webforms.md) on any device (computer, iPhone, Android).
3. Alternatively, download and set up the [KoboCollect](kobocollect_on_android_latest.md) Android application for mobile data collection.


<p class="note">
    <strong>Note:</strong> To <a href="project_sharing_settings.html">share your form</a> with anyone with the form URL, enable "Allow submissions to this form without a username and password" in the <strong>{{ui:form|upper}}</strong> page, under <strong>{{ui:Collect data}}</strong>.
</p>


Once you have collected data, you can view, edit, and download it from the {{ui:data|upper,bold}} page of your project. To learn more about managing your data, see the [Managing Projects & Data](https://support.kobotoolbox.org/managing-projects.html) support section.